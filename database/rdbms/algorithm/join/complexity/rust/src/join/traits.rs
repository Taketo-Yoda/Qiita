use crate::data::{TableData, IndexData, TableRecord};
use std::time::Duration;

pub trait JoinAlgorithm {
    fn execute(
        &self,
        inner_table: &TableData,
        inner_index: Option<&IndexData>,
        outer_table: &TableData,
        outer_index: Option<&IndexData>,
        filter_value: u64,
        fetch_ratio: f64,
    ) -> JoinResult;

    fn algorithm_name(&self) -> &str;
}

#[derive(Debug)]
pub struct JoinResult {
    pub matched_records: Vec<(TableRecord, TableRecord)>,
    pub metrics: JoinMetrics,
}

#[derive(Debug)]
pub struct JoinMetrics {
    pub duration: Duration,
    pub inner_accesses: usize,
    pub outer_accesses: usize,
    pub result_count: usize,
    pub algorithm: String,
}
