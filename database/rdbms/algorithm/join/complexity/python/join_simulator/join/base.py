"""結合アルゴリズムの基底クラスと結果型

JoinAlgorithm抽象基底クラス、JoinMetrics、JoinResultを提供
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Tuple
from ..data.table import TableData, IndexData, TableRecord


@dataclass
class JoinMetrics:
    """結合実行の計測メトリクス

    Attributes:
        duration_ms: 実行時間（ミリ秒）
        inner_accesses: 内部表アクセス回数
        outer_accesses: 外部表アクセス回数
        result_count: 結合結果のレコード数
        algorithm: アルゴリズム名
    """
    duration_ms: float
    inner_accesses: int
    outer_accesses: int
    result_count: int
    algorithm: str


@dataclass
class JoinResult:
    """結合実行結果

    Attributes:
        matched_records: 結合されたレコードのペアのリスト
        metrics: 実行メトリクス
    """
    matched_records: List[Tuple[TableRecord, TableRecord]]
    metrics: JoinMetrics


class JoinAlgorithm(ABC):
    """結合アルゴリズムの抽象基底クラス

    全ての結合アルゴリズム実装はこのクラスを継承する。
    """

    @abstractmethod
    def execute(
        self,
        inner_table: TableData,
        inner_index: Optional[IndexData],
        outer_table: TableData,
        outer_index: Optional[IndexData],
        filter_value: int,
        fetch_ratio: float,
    ) -> JoinResult:
        """結合を実行

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
        pass

    @abstractmethod
    def algorithm_name(self) -> str:
        """アルゴリズム名を取得

        Returns:
            アルゴリズム名
        """
        pass
