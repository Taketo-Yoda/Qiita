"""計算量解析

Big-O計算量の算出と表示
"""

import math
from ..cli import CliArgs, JoinAlgorithmType


def calculate_complexity(
    args: CliArgs,
    inner_accesses: int,
    outer_accesses: int,
) -> str:
    """Big-O計算量を算出

    実行パラメータとアクセス回数から、理論的な計算量を算出して
    わかりやすい形式で文字列化。

    Args:
        args: CLI引数
        inner_accesses: 実際の内部表アクセス回数
        outer_accesses: 実際の外部表アクセス回数

    Returns:
        計算量の説明文字列
    """
    n = args.inner_total * 10_000
    m = int((n * args.fetch_ratio / 100.0) + 0.5)
    c = args.outer_total * 10_000
    d = int(args.join_factor)

    log_n = math.log2(n) if n > 0 else 0
    log_c = math.log2(c) if c > 0 else 0

    if args.join_algorithm == JoinAlgorithmType.NESTED_LOOP:
        if args.inner_use_index and args.outer_use_index:
            return (
                f"Nested Loop Join (両方インデックス使用)\n"
                f"  内部表スキャン: O(log n + m) = O(log {n} + {m}) ≈ {inner_accesses}\n"
                f"  外部表スキャン: O(m × (log c + d)) = O({m} × (log {c} + {d})) ≈ {outer_accesses}\n"
                f"  総計算量: O(m × log c) where m={m}, c={c}"
            )
        elif args.inner_use_index and not args.outer_use_index:
            return (
                f"Nested Loop Join (内部表のみインデックス使用)\n"
                f"  内部表スキャン: O(log n + m) = O(log {n} + {m}) ≈ {inner_accesses}\n"
                f"  外部表スキャン: O(m × c) = O({m} × {c}) ≈ {outer_accesses}\n"
                f"  総計算量: O(m × c) where m={m}, c={c}"
            )
        elif not args.inner_use_index and args.outer_use_index:
            return (
                f"Nested Loop Join (外部表のみインデックス使用)\n"
                f"  内部表スキャン: O(n) = O({n}) ≈ {inner_accesses}\n"
                f"  外部表スキャン: O(m × (log c + d)) = O({m} × (log {c} + {d})) ≈ {outer_accesses}\n"
                f"  総計算量: O(n + m × log c) where n={n}, m={m}, c={c}"
            )
        else:
            return (
                f"Nested Loop Join (インデックス未使用)\n"
                f"  内部表スキャン: O(n) = O({n}) ≈ {inner_accesses}\n"
                f"  外部表スキャン: O(m × c) = O({m} × {c}) ≈ {outer_accesses}\n"
                f"  総計算量: O(m × c) where m={m}, c={c}"
            )
    else:  # Hash Join
        if args.inner_use_index:
            return (
                f"Hash Join (内部表インデックス使用)\n"
                f"  内部表スキャン: O(log n + m) = O(log {n} + {m}) ≈ {inner_accesses}\n"
                f"  Build Phase: O(m) = O({m})\n"
                f"  Probe Phase: O(c) = O({c}) ≈ {outer_accesses}\n"
                f"  総計算量: O(m + c) where m={m}, c={c}"
            )
        else:
            return (
                f"Hash Join (インデックス未使用)\n"
                f"  内部表スキャン: O(n) = O({n}) ≈ {inner_accesses}\n"
                f"  Build Phase: O(m) = O({m})\n"
                f"  Probe Phase: O(c) = O({c}) ≈ {outer_accesses}\n"
                f"  総計算量: O(n + m + c) where n={n}, m={m}, c={c}"
            )
