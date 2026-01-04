mod cli;
mod data;
mod join;
mod metrics;

use clap::Parser;
use cli::{Cli, JoinAlgorithmType};
use data::TableGenerator;
use join::{JoinAlgorithm, NestedLoopJoin, HashJoin};
use metrics::calculate_complexity;

fn main() {
    let cli = Cli::parse();

    if let Err(e) = cli.validate() {
        eprintln!("Error: {}", e);
        std::process::exit(1);
    }

    println!("=== RDBMS Join Algorithm Simulator ===");
    println!("Inner table: {} records", cli.inner_total * 10_000);
    println!("Fetch ratio: {}%", cli.fetch_ratio);
    println!("Inner index: {}", cli.inner_use_index);
    println!("Join algorithm: {:?}", cli.join_algorithm);
    println!("Outer table: {} records", cli.outer_total * 10_000);
    println!("Join factor: {}", cli.join_factor);
    println!("Outer index: {}", cli.outer_use_index);
    println!();

    println!("Generating test data...");
    let mut generator = TableGenerator::new();

    let ((inner_table, inner_index), (outer_table, outer_index)) = generator.generate_matched_tables(
        cli.inner_total * 10_000,
        cli.fetch_ratio,
        cli.outer_total * 10_000,
        cli.join_factor,
    );

    println!("Data generation completed.");
    println!();

    let join_algo: Box<dyn JoinAlgorithm> = match cli.join_algorithm {
        JoinAlgorithmType::NestedLoop => {
            Box::new(NestedLoopJoin::new(cli.outer_use_index))
        }
        JoinAlgorithmType::Hash => Box::new(HashJoin::new()),
    };

    println!("Executing join...");
    let result = join_algo.execute(
        &inner_table,
        if cli.inner_use_index { Some(&inner_index) } else { None },
        &outer_table,
        if cli.outer_use_index { Some(&outer_index) } else { None },
        cli.filter_value,
        cli.fetch_ratio,
    );

    println!();
    println!("=== Results ===");
    println!("Algorithm: {}", result.metrics.algorithm);
    println!("Execution time: {:?}", result.metrics.duration);
    println!("Inner table accesses: {}", result.metrics.inner_accesses);
    println!("Outer table accesses: {}", result.metrics.outer_accesses);
    println!("Result count: {}", result.metrics.result_count);
    println!();

    println!("=== Complexity Analysis ===");
    let complexity = calculate_complexity(
        &cli,
        result.metrics.inner_accesses,
        result.metrics.outer_accesses,
    );
    println!("{}", complexity);
}
