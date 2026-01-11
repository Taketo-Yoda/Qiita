"""Hash Join実装

Hash Joinアルゴリズムを提供
"""

import time
from typing import Dict, List, Optional, Tuple
from .base import JoinAlgorithm, JoinResult, JoinMetrics
from ..data.table import TableData, IndexData, TableRecord


class HashJoin(JoinAlgorithm):
    """Hash Join実装

    内部表でハッシュテーブルを構築し、外部表をスキャンして
    ハッシュ検索で結合するアルゴリズム。

    計算量:
        - インデックス使用: O(log n + m + c)
        - フルスキャン: O(n + m + c)
        ※ n: 内部表件数, m: フェッチ件数, c: 外部表件数

    フェーズ:
        1. 内部表フェッチ（WHERE条件）
        2. Build Phase: 内部表レコードでハッシュテーブル構築
        3. Probe Phase: 外部表をスキャンしてハッシュ検索
    """

    def execute(
        self,
        inner_table: TableData,
        inner_index: Optional[IndexData],
        outer_table: TableData,
        outer_index: Optional[IndexData],  # Hash Joinでは使用しない
        filter_value: int,
        fetch_ratio: float,
    ) -> JoinResult:
        """Hash Joinを実行

        Args:
            inner_table: 内部表
            inner_index: 内部表インデックス（Noneの場合はフルスキャン）
            outer_table: 外部表
            outer_index: 外部表インデックス（Hash Joinでは未使用）
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

        # フェーズ2: Build Phase - ハッシュテーブル構築
        # column_value -> [TableRecord, ...]
        hash_table: Dict[int, List[TableRecord]] = {}
        for inner_rec in inner_records:
            key = inner_rec.column_value
            if key not in hash_table:
                hash_table[key] = []
            hash_table[key].append(inner_rec)

        # フェーズ3: Probe Phase - 外部表スキャン
        outer_accesses += len(outer_table)
        for outer_rec in outer_table.iter():
            # ハッシュテーブルから検索: O(1)平均
            if outer_rec.filter_key in hash_table:
                for inner_rec in hash_table[outer_rec.filter_key]:
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
            "Hash Join"
        """
        return "Hash Join"
