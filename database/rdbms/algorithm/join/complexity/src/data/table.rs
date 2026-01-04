use std::collections::BTreeMap;

#[derive(Debug, Clone)]
pub struct TableRecord {
    pub primary_key: u64,
    pub filter_key: u64,
    pub column_value: u64,
}

#[derive(Debug)]
pub struct TableData {
    records: Vec<TableRecord>,
    pk_index: BTreeMap<u64, usize>,
}

impl TableData {
    pub fn new(capacity: usize) -> Self {
        Self {
            records: Vec::with_capacity(capacity),
            pk_index: BTreeMap::new(),
        }
    }

    pub fn insert(&mut self, record: TableRecord) {
        let idx = self.records.len();
        self.pk_index.insert(record.primary_key, idx);
        self.records.push(record);
    }

    pub fn get_by_pk(&self, pk: u64) -> Option<&TableRecord> {
        self.pk_index.get(&pk).and_then(|&idx| self.records.get(idx))
    }

    pub fn iter(&self) -> impl Iterator<Item = &TableRecord> {
        self.records.iter()
    }

    pub fn len(&self) -> usize {
        self.records.len()
    }

    #[allow(dead_code)]
    pub fn is_empty(&self) -> bool {
        self.records.is_empty()
    }
}

#[derive(Debug)]
pub struct IndexData {
    index: BTreeMap<u64, Vec<u64>>,
}

impl IndexData {
    pub fn new() -> Self {
        Self {
            index: BTreeMap::new(),
        }
    }

    pub fn insert(&mut self, filter_key: u64, primary_key: u64) {
        self.index
            .entry(filter_key)
            .or_insert_with(Vec::new)
            .push(primary_key);
    }

    pub fn search(&self, filter_key: u64) -> Option<&Vec<u64>> {
        self.index.get(&filter_key)
    }

    #[allow(dead_code)]
    pub fn len(&self) -> usize {
        self.index.values().map(|v| v.len()).sum()
    }

    #[allow(dead_code)]
    pub fn is_empty(&self) -> bool {
        self.index.is_empty()
    }
}

impl Default for IndexData {
    fn default() -> Self {
        Self::new()
    }
}
