use rand::Rng;
use super::table::{TableData, TableRecord, IndexData};

pub struct TableGenerator {
    rng: rand::rngs::ThreadRng,
}

impl TableGenerator {
    pub fn new() -> Self {
        Self {
            rng: rand::thread_rng(),
        }
    }

    pub fn generate_inner_table(
        &mut self,
        total_records: usize,
        filter_key_range: u64,
    ) -> (TableData, IndexData) {
        let mut table = TableData::new(total_records);
        let mut index = IndexData::new();

        for i in 0..total_records {
            let pk = i as u64;
            let filter_key = self.rng.gen_range(0..filter_key_range);
            let column_value = self.rng.gen_range(0..1_000_000);

            let record = TableRecord {
                primary_key: pk,
                filter_key,
                column_value,
            };

            index.insert(filter_key, pk);
            table.insert(record);
        }

        (table, index)
    }

    pub fn generate_matched_tables(
        &mut self,
        inner_total: usize,
        fetch_ratio: f64,
        outer_total: usize,
        join_factor: usize,
    ) -> ((TableData, IndexData), (TableData, IndexData)) {
        let mut inner_table = TableData::new(inner_total);
        let mut inner_index = IndexData::new();
        let mut outer_table = TableData::new(outer_total);
        let mut outer_index = IndexData::new();

        let column_values: Vec<u64> = (0..inner_total)
            .map(|_| self.rng.gen_range(0..100_000))
            .collect();

        for (i, &col_val) in column_values.iter().enumerate() {
            let record = TableRecord {
                primary_key: i as u64,
                filter_key: self.rng.gen_range(0..100),
                column_value: col_val,
            };
            inner_index.insert(record.filter_key, record.primary_key);
            inner_table.insert(record);
        }

        let fetch_count = (inner_total as f64 * fetch_ratio / 100.0).ceil() as usize;
        let required_matches = fetch_count * join_factor;

        for i in 0..outer_total {
            let filter_key = if i < required_matches {
                column_values[i % fetch_count]
            } else {
                self.rng.gen_range(0..100_000)
            };

            let record = TableRecord {
                primary_key: i as u64,
                filter_key,
                column_value: self.rng.gen_range(0..100_000),
            };
            outer_index.insert(record.filter_key, record.primary_key);
            outer_table.insert(record);
        }

        ((inner_table, inner_index), (outer_table, outer_index))
    }
}

impl Default for TableGenerator {
    fn default() -> Self {
        Self::new()
    }
}
