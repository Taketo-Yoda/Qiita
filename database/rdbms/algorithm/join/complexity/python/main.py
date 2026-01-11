#!/usr/bin/env python3
"""RDBMS Join Algorithm Simulator - メインエントリーポイント

RDBMSのテーブル結合アルゴリズム(Nested Loop Join, Hash Join)を
シミュレートし、性能を測定するCLIツール。
"""

from join_simulator.cli import parse_args, JoinAlgorithmType
from join_simulator.data.generator import TableGenerator
from join_simulator.join.nested_loop import NestedLoopJoin
from join_simulator.join.hash_join import HashJoin
from join_simulator.metrics.complexity import calculate_complexity


def main() -> None:
    """メイン処理"""
    # CLI引数をパース
    args = parse_args()

    # パラメータ表示
    print("=" * 60)
    print("RDBMS Join Algorithm Simulator")
    print("=" * 60)
    print(f"内部表: {args.inner_total * 10_000:,} レコード")
    print(f"フェッチ比率: {args.fetch_ratio}%")
    print(f"内部表インデックス: {'使用' if args.inner_use_index else '未使用'}")
    print(f"結合アルゴリズム: {args.join_algorithm.value}")
    print(f"外部表: {args.outer_total * 10_000:,} レコード")
    print(f"結合係数: {args.join_factor}")
    print(f"外部表インデックス: {'使用' if args.outer_use_index else '未使用'}")
    print(f"WHERE条件値: {args.filter_value}")
    print()

    # テストデータ生成
    print("テストデータを生成中...")
    generator = TableGenerator()

    (inner_table, inner_index), (outer_table, outer_index) = generator.generate_matched_tables(
        inner_total=args.inner_total * 10_000,
        fetch_ratio=args.fetch_ratio,
        outer_total=args.outer_total * 10_000,
        join_factor=int(args.join_factor) if args.join_factor >= 1 else 1,
    )

    print(f"  内部表: {len(inner_table):,} レコード生成")
    print(f"  外部表: {len(outer_table):,} レコード生成")
    print("データ生成完了")
    print()

    # アルゴリズム選択
    if args.join_algorithm == JoinAlgorithmType.NESTED_LOOP:
        join_algo = NestedLoopJoin(use_outer_index=args.outer_use_index)
    else:
        join_algo = HashJoin()

    # 結合実行
    print("結合を実行中...")
    result = join_algo.execute(
        inner_table=inner_table,
        inner_index=inner_index if args.inner_use_index else None,
        outer_table=outer_table,
        outer_index=outer_index if args.outer_use_index else None,
        filter_value=args.filter_value,
        fetch_ratio=args.fetch_ratio,
    )

    # 結果表示
    print()
    print("=" * 60)
    print("実行結果")
    print("=" * 60)
    print(f"アルゴリズム: {result.metrics.algorithm}")
    print(f"実行時間: {result.metrics.duration_ms:.3f} ms")
    print(f"内部表アクセス回数: {result.metrics.inner_accesses:,}")
    print(f"外部表アクセス回数: {result.metrics.outer_accesses:,}")
    print(f"結合結果件数: {result.metrics.result_count:,}")
    print()

    # Big-O計算量表示
    print("=" * 60)
    print("計算量解析")
    print("=" * 60)
    complexity = calculate_complexity(args, result.metrics.inner_accesses, result.metrics.outer_accesses)
    print(complexity)
    print()


if __name__ == "__main__":
    main()
