use std::time::Instant;
use crate::data::{TableData, IndexData};
use crate::join::traits::{JoinAlgorithm, JoinResult, JoinMetrics};

pub struct NestedLoopJoin {
    use_outer_index: bool,
}

impl NestedLoopJoin {
    pub fn new(use_outer_index: bool) -> Self {
        Self { use_outer_index }
    }
}

impl JoinAlgorithm for NestedLoopJoin {
    fn execute(
        &self,
        inner_table: &TableData,
        inner_index: Option<&IndexData>,
        outer_table: &TableData,
        outer_index: Option<&IndexData>,
        filter_value: u64,
        fetch_ratio: f64,
    ) -> JoinResult {
        let start = Instant::now();
        let mut matched = Vec::new();
        let mut inner_accesses = 0;
        let mut outer_accesses = 0;

        let inner_records: Vec<_> = if let Some(idx) = inner_index {
            inner_accesses += 1;
            idx.search(filter_value)
                .map(|pks| {
                    pks.iter()
                        .filter_map(|&pk| inner_table.get_by_pk(pk))
                        .collect()
                })
                .unwrap_or_default()
        } else {
            inner_accesses += inner_table.len();
            inner_table
                .iter()
                .filter(|r| r.filter_key == filter_value)
                .collect()
        };

        let fetch_count = (inner_records.len() as f64 * fetch_ratio / 100.0).ceil() as usize;
        let inner_records = &inner_records[..fetch_count.min(inner_records.len())];

        for inner_rec in inner_records {
            if self.use_outer_index {
                if let Some(outer_idx) = outer_index {
                    outer_accesses += 1;
                    if let Some(pks) = outer_idx.search(inner_rec.column_value) {
                        for &pk in pks {
                            if let Some(outer_rec) = outer_table.get_by_pk(pk) {
                                outer_accesses += 1;
                                matched.push(((*inner_rec).clone(), outer_rec.clone()));
                            }
                        }
                    }
                }
            } else {
                outer_accesses += outer_table.len();
                for outer_rec in outer_table.iter() {
                    if outer_rec.filter_key == inner_rec.column_value {
                        matched.push(((*inner_rec).clone(), outer_rec.clone()));
                    }
                }
            }
        }

        let duration = start.elapsed();

        let metrics = JoinMetrics {
            duration,
            inner_accesses,
            outer_accesses,
            result_count: matched.len(),
            algorithm: self.algorithm_name().to_string(),
        };

        JoinResult {
            matched_records: matched,
            metrics,
        }
    }

    fn algorithm_name(&self) -> &str {
        "Nested Loop Join"
    }
}
