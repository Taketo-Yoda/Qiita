"""Nested Loop Join実装

Nested Loop Joinアルゴリズムを提供
"""

import time
from typing import List, Optional, Tuple
from .base import JoinAlgorithm, JoinResult, JoinMetrics
from ..data.table import TableData, IndexData, TableRecord


class NestedLoopJoin(JoinAlgorithm):
    """Nested Loop Join実装

    内部表の各レコードに対して、外部表を逐次スキャンする結合アルゴリズム。
    インデックスを使用することでスキャン効率を向上可能。

    計算量:
        - 両方インデックス使用: O(log n + m × log c)
        - 両方フルスキャン: O(n + m × c)
        ※ n: 内部表件数, m: フェッチ件数, c: 外部表件数
    """

    def __init__(self, use_outer_index: bool) -> None:
        """初期化

        Args:
            use_outer_index: 外部表のインデックスを使用するか
        """
        self._use_outer_index = use_outer_index

    def execute(
        self,
        inner_table: TableData,
        inner_index: Optional[IndexData],
        outer_table: TableData,
        outer_index: Optional[IndexData],
        filter_value: int,
        fetch_ratio: float,
    ) -> JoinResult:
        """Nested Loop Joinを実行

        Args:
            inner_table: 内部表
            inner_index: 内部表インデックス（Noneの場合はフルスキャン）
            outer_table: 外部表
            outer_index: 外部表インデックス（Noneの場合はフルスキャン）
            filter_value: WHERE条件のフィルタ値
            fetch_ratio: 内部表のフェッチ比率(%)

        Returns:
            結合結果
        """
        start = time.time()
        matched: List[Tuple[TableRecord, TableRecord]] = []
        inner_accesses = 0
        outer_accesses = 0

        # フェーズ1: 内部表フェッチ（WHERE条件）
        if inner_index is not None:
            # インデックス使用: O(log n)
            inner_accesses += 1
            pks = inner_index.search(filter_value)
            if pks:
                inner_records = [inner_table.get_by_pk(pk) for pk in pks]
                inner_records = [r for r in inner_records if r is not None]
            else:
                inner_records = []
        else:
            # フルスキャン: O(n)
            inner_accesses += len(inner_table)
            inner_records = [r for r in inner_table.iter() if r.filter_key == filter_value]

        # fetch_ratio適用
        fetch_count = int((len(inner_records) * fetch_ratio / 100.0) + 0.5)  # ceil
        inner_records = inner_records[:min(fetch_count, len(inner_records))]

        # フェーズ2: Nested Loop（ON条件）
        for inner_rec in inner_records:
            if self._use_outer_index and outer_index is not None:
                # 外部表インデックス使用: O(log c)
                outer_accesses += 1
                pks = outer_index.search(inner_rec.column_value)
                if pks:
                    for pk in pks:
                        outer_rec = outer_table.get_by_pk(pk)
                        if outer_rec:
                            outer_accesses += 1
                            matched.append((inner_rec, outer_rec))
            else:
                # 外部表フルスキャン: O(c)
                outer_accesses += len(outer_table)
                for outer_rec in outer_table.iter():
                    if outer_rec.filter_key == inner_rec.column_value:
                        matched.append((inner_rec, outer_rec))

        duration_ms = (time.time() - start) * 1000

        metrics = JoinMetrics(
            duration_ms=duration_ms,
            inner_accesses=inner_accesses,
            outer_accesses=outer_accesses,
            result_count=len(matched),
            algorithm=self.algorithm_name(),
        )

        return JoinResult(matched_records=matched, metrics=metrics)

    def algorithm_name(self) -> str:
        """アルゴリズム名を取得

        Returns:
            "Nested Loop Join"
        """
        return "Nested Loop Join"
