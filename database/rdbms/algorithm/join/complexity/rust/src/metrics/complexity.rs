use crate::cli::{Cli, JoinAlgorithmType};

pub fn calculate_complexity(
    cli: &Cli,
    inner_accesses: usize,
    outer_accesses: usize,
) -> String {
    let n = cli.inner_total * 10_000;
    let m = (n as f64 * cli.fetch_ratio / 100.0).ceil() as usize;
    let c = cli.outer_total * 10_000;
    let d = cli.join_factor;

    match cli.join_algorithm {
        JoinAlgorithmType::NestedLoop => {
            if cli.inner_use_index && cli.outer_use_index {
                format!(
                    "Nested Loop Join (両方インデックス使用)\n\
                     Inner scan: O(log n + m) = O(log {} + {}) ≈ {}\n\
                     Outer scan: O(m * (log c + d)) = O({} * (log {} + {})) ≈ {}\n\
                     Total: O(m * log c) where m={}, c={}",
                    n, m, inner_accesses,
                    m, c, d, outer_accesses,
                    m, c
                )
            } else if cli.inner_use_index && !cli.outer_use_index {
                format!(
                    "Nested Loop Join (駆動表のみインデックス使用)\n\
                     Inner scan: O(log n + m) = O(log {} + {}) ≈ {}\n\
                     Outer scan: O(m * c) = O({} * {}) ≈ {}\n\
                     Total: O(m * c) where m={}, c={}",
                    n, m, inner_accesses,
                    m, c, outer_accesses,
                    m, c
                )
            } else if !cli.inner_use_index && cli.outer_use_index {
                format!(
                    "Nested Loop Join (外部表のみインデックス使用)\n\
                     Inner scan: O(n) = O({}) ≈ {}\n\
                     Outer scan: O(m * (log c + d)) = O({} * (log {} + {})) ≈ {}\n\
                     Total: O(n + m * log c) where n={}, m={}, c={}",
                    n, inner_accesses,
                    m, c, d, outer_accesses,
                    n, m, c
                )
            } else {
                format!(
                    "Nested Loop Join (インデックス未使用)\n\
                     Inner scan: O(n) = O({}) ≈ {}\n\
                     Outer scan: O(m * c) = O({} * {}) ≈ {}\n\
                     Total: O(m * c) where m={}, c={}",
                    n, inner_accesses,
                    m, c, outer_accesses,
                    m, c
                )
            }
        }
        JoinAlgorithmType::Hash => {
            if cli.inner_use_index {
                format!(
                    "Hash Join (駆動表インデックス使用)\n\
                     Inner scan: O(log n + m) = O(log {} + {}) ≈ {}\n\
                     Build phase: O(m) = O({})\n\
                     Probe phase: O(c) = O({}) ≈ {}\n\
                     Total: O(m + c) where m={}, c={}",
                    n, m, inner_accesses,
                    m,
                    c, outer_accesses,
                    m, c
                )
            } else {
                format!(
                    "Hash Join (インデックス未使用)\n\
                     Inner scan: O(n) = O({}) ≈ {}\n\
                     Build phase: O(m) = O({})\n\
                     Probe phase: O(c) = O({}) ≈ {}\n\
                     Total: O(n + m + c) where n={}, m={}, c={}",
                    n, inner_accesses,
                    m,
                    c, outer_accesses,
                    n, m, c
                )
            }
        }
    }
}
