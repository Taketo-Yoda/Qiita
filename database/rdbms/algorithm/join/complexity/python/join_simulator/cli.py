"""CLI引数パーサー

コマンドライン引数の解析とバリデーション
"""

import argparse
from enum import Enum
from dataclasses import dataclass


class JoinAlgorithmType(Enum):
    """結合アルゴリズム種別"""
    NESTED_LOOP = "nlj"
    HASH = "hj"


@dataclass
class CliArgs:
    """CLI引数

    Attributes:
        inner_total: 内部表母数（万件）
        fetch_ratio: フェッチ比率（%）
        inner_use_index: 内部表インデックス使用
        join_algorithm: 結合アルゴリズム種別
        outer_total: 外部表母数（万件）
        join_factor: 外部表一致比率
        outer_use_index: 外部表インデックス使用
        filter_value: WHERE条件のフィルタ値
    """
    inner_total: int
    fetch_ratio: float
    inner_use_index: bool
    join_algorithm: JoinAlgorithmType
    outer_total: int
    join_factor: float
    outer_use_index: bool
    filter_value: int

    def validate(self) -> None:
        """制約条件をバリデート

        Raises:
            ValueError: バリデーションエラー
        """
        if not (0 < self.fetch_ratio <= 100):
            raise ValueError("fetch_ratioは1-100の範囲で指定してください")

        if self.join_factor < 0.01:
            raise ValueError("join_factorは0.01以上で指定してください")

        inner_records = self.inner_total * 10_000
        outer_records = self.outer_total * 10_000
        fetch_count = int((inner_records * self.fetch_ratio / 100.0) + 0.5)
        required_matches = int(fetch_count * self.join_factor)

        if required_matches > outer_records:
            raise ValueError(
                f"制約違反: フェッチ件数({fetch_count}) × 一致比率({self.join_factor}) "
                f"= {required_matches} が外部表件数({outer_records})を超えています"
            )

        if self.join_algorithm == JoinAlgorithmType.HASH and self.outer_use_index:
            print("警告: Hash Joinでは外部表インデックスは使用されません")


def parse_args() -> CliArgs:
    """CLI引数をパース

    Returns:
        パース済みCLI引数

    Raises:
        ValueError: バリデーションエラー
    """
    parser = argparse.ArgumentParser(
        prog="join-sim",
        description="RDBMS Join Algorithm Complexity Simulator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # Nested Loop Join（両方インデックス使用）
  %(prog)s -a 10 -b 50 --inner-use-index -j nlj -c 100 -d 5 --outer-use-index

  # Hash Join（内部表のみインデックス使用）
  %(prog)s -a 5 -b 100 --inner-use-index -j hj -c 50 -d 2

パラメータ説明:
  -a: 内部表の母数（万件単位）
  -b: WHERE条件でフェッチする比率（%%）
  -j: 結合アルゴリズム（nlj=Nested Loop, hj=Hash Join）
  -c: 外部表の母数（万件単位）
  -d: 外部表との一致比率（1.0=1:1結合）
        """,
    )

    parser.add_argument(
        "-a",
        "--inner-total",
        type=int,
        required=True,
        metavar="NUM",
        help="内部表母数（万件）",
    )

    parser.add_argument(
        "-b",
        "--fetch-ratio",
        type=float,
        required=True,
        metavar="PERCENT",
        help="内部表フェッチ比率（1-100%%）",
    )

    parser.add_argument(
        "--inner-use-index",
        action="store_true",
        help="内部表でインデックスを使用",
    )

    parser.add_argument(
        "-j",
        "--join-algorithm",
        type=str,
        required=True,
        choices=["nlj", "hj"],
        metavar="ALG",
        help="結合アルゴリズム（nlj=Nested Loop, hj=Hash Join）",
    )

    parser.add_argument(
        "-c",
        "--outer-total",
        type=int,
        required=True,
        metavar="NUM",
        help="外部表母数（万件）",
    )

    parser.add_argument(
        "-d",
        "--join-factor",
        type=float,
        required=True,
        metavar="NUM",
        help="外部表一致比率（0.01以上、1.0=1:1結合）",
    )

    parser.add_argument(
        "--outer-use-index",
        action="store_true",
        help="外部表でインデックスを使用（NLJのみ有効）",
    )

    parser.add_argument(
        "--filter-value",
        type=int,
        default=20,
        metavar="VAL",
        help="WHERE条件のフィルタ値（デフォルト: 20）",
    )

    args = parser.parse_args()

    cli_args = CliArgs(
        inner_total=args.inner_total,
        fetch_ratio=args.fetch_ratio,
        inner_use_index=args.inner_use_index,
        join_algorithm=JoinAlgorithmType(args.join_algorithm),
        outer_total=args.outer_total,
        join_factor=args.join_factor,
        outer_use_index=args.outer_use_index,
        filter_value=args.filter_value,
    )

    cli_args.validate()
    return cli_args
