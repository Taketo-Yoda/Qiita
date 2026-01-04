use std::collections::HashMap;
use std::time::Instant;
use crate::data::{TableData, IndexData, TableRecord};
use crate::join::traits::{JoinAlgorithm, JoinResult, JoinMetrics};

pub struct HashJoin;

impl HashJoin {
    pub fn new() -> Self {
        Self
    }
}

impl Default for HashJoin {
    fn default() -> Self {
        Self::new()
    }
}

impl JoinAlgorithm for HashJoin {
    fn execute(
        &self,
        inner_table: &TableData,
        inner_index: Option<&IndexData>,
        outer_table: &TableData,
        _outer_index: Option<&IndexData>,
        filter_value: u64,
        fetch_ratio: f64,
    ) -> JoinResult {
        let start = Instant::now();
        let mut matched = Vec::new();
        let mut inner_accesses = 0;
        let mut outer_accesses = 0;

        let inner_records: Vec<&TableRecord> = if let Some(idx) = inner_index {
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

        let mut hash_table: HashMap<u64, Vec<&TableRecord>> = HashMap::new();
        for &inner_rec in inner_records {
            hash_table
                .entry(inner_rec.column_value)
                .or_insert_with(Vec::new)
                .push(inner_rec);
        }

        outer_accesses += outer_table.len();
        for outer_rec in outer_table.iter() {
            if let Some(inner_recs) = hash_table.get(&outer_rec.filter_key) {
                for &inner_rec in inner_recs {
                    matched.push((inner_rec.clone(), outer_rec.clone()));
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
        "Hash Join"
    }
}
