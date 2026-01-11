use clap::{Parser, ValueEnum};

#[derive(Parser, Debug)]
#[command(name = "join-sim")]
#[command(about = "RDBMS Join Algorithm Complexity Simulator", long_about = None)]
pub struct Cli {
    #[arg(short = 'a', long, value_name = "NUM")]
    pub inner_total: usize,

    #[arg(short = 'b', long, value_name = "PERCENT", value_parser = validate_percentage)]
    pub fetch_ratio: f64,

    #[arg(long)]
    pub inner_use_index: bool,

    #[arg(short = 'j', long, value_enum)]
    pub join_algorithm: JoinAlgorithmType,

    #[arg(short = 'c', long, value_name = "NUM")]
    pub outer_total: usize,

    #[arg(short = 'd', long, value_name = "NUM", value_parser = validate_join_factor)]
    pub join_factor: usize,

    #[arg(long)]
    pub outer_use_index: bool,

    #[arg(long, default_value_t = 20)]
    pub filter_value: u64,
}

#[derive(Debug, Clone, ValueEnum)]
pub enum JoinAlgorithmType {
    #[value(name = "nl")]
    NestedLoop,
    #[value(name = "hash")]
    Hash,
}

fn validate_percentage(s: &str) -> Result<f64, String> {
    let val: f64 = s.parse().map_err(|_| format!("Invalid percentage: {}", s))?;
    if val > 0.0 && val <= 100.0 {
        Ok(val)
    } else {
        Err("Percentage must be between 0 and 100".to_string())
    }
}

fn validate_join_factor(s: &str) -> Result<usize, String> {
    let val: usize = s.parse().map_err(|_| format!("Invalid join factor: {}", s))?;
    if val >= 1 {
        Ok(val)
    } else {
        Err("Join factor must be >= 1".to_string())
    }
}

impl Cli {
    pub fn validate(&self) -> Result<(), String> {
        let inner_records = self.inner_total * 10_000;
        let outer_records = self.outer_total * 10_000;
        let required_outer = inner_records * self.join_factor;

        if required_outer > outer_records {
            return Err(format!(
                "Constraint violation: a * 10000 * d ({}) > c * 10000 ({})",
                required_outer, outer_records
            ));
        }

        if matches!(self.join_algorithm, JoinAlgorithmType::Hash) && self.outer_use_index {
            eprintln!("Warning: --outer-use-index is ignored for Hash Join");
        }

        Ok(())
    }
}
