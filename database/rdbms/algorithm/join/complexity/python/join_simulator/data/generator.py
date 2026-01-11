"""テストデータ生成器

結合可能なテーブルペアを生成
"""

import random
from typing import Tuple, Optional
from .table import TableData, IndexData, TableRecord


class TableGenerator:
    """テストデータ生成器

    RDBMSのテーブル結合シミュレーション用のテストデータを生成。
    内部表と外部表の結合関係を制御可能。
    """

    def __init__(self, seed: Optional[int] = None) -> None:
        """初期化

        Args:
            seed: 乱数シード（再現性のため）
        """
        self._rng = random.Random(seed)

    def generate_matched_tables(
        self,
        inner_total: int,
        fetch_ratio: float,
        outer_total: int,
        join_factor: int,
    ) -> Tuple[Tuple[TableData, IndexData], Tuple[TableData, IndexData]]:
        """結合可能なテーブルペアを生成

        内部表と外部表を生成し、指定されたjoin_factorに基づいて
        確実に結合が発生するようにデータを調整。

        Args:
            inner_total: 内部表のレコード数
            fetch_ratio: 内部表のフェッチ比率(%)
            outer_total: 外部表のレコード数
            join_factor: 結合係数（内部表の1レコードに対する外部表のマッチ数）

        Returns:
            ((内部表, 内部表インデックス), (外部表, 外部表インデックス))のタプル
        """
        inner_table = TableData(inner_total)
        inner_index = IndexData()
        outer_table = TableData(outer_total)
        outer_index = IndexData()

        # 内部表のcolumn_valueを事前生成
        # これらの値を外部表のfilter_keyとして使用することで結合を保証
        column_values = [self._rng.randrange(0, 100_000) for _ in range(inner_total)]

        # 内部表を生成
        for i, col_val in enumerate(column_values):
            record = TableRecord(
                primary_key=i,
                filter_key=self._rng.randrange(0, 100),
                column_value=col_val,
            )
            inner_index.insert(record.filter_key, record.primary_key)
            inner_table.insert(record)

        # fetch_ratioに基づいてフェッチされるレコード数を計算
        fetch_count = int((inner_total * fetch_ratio / 100.0) + 0.5)  # ceil
        # 必要な結合数を計算
        required_matches = fetch_count * join_factor

        # 外部表を生成
        for i in range(outer_total):
            # 最初のrequired_matches件は確実に結合するよう、
            # 内部表のcolumn_valueを使用
            if i < required_matches:
                filter_key = column_values[i % fetch_count]
            else:
                # 残りはランダム値（結合しない可能性が高い）
                filter_key = self._rng.randrange(0, 100_000)

            record = TableRecord(
                primary_key=i,
                filter_key=filter_key,
                column_value=self._rng.randrange(0, 100_000),
            )
            outer_index.insert(record.filter_key, record.primary_key)
            outer_table.insert(record)

        return ((inner_table, inner_index), (outer_table, outer_index))
