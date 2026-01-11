"""テーブルとインデックスのデータ構造

TableRecord, TableData, IndexDataを提供
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Iterator
import bisect


@dataclass
class TableRecord:
    """テーブルレコード

    Attributes:
        primary_key: 主キー
        filter_key: WHERE条件で使用するフィルタキー
        column_value: JOIN条件で使用するカラム値
    """
    primary_key: int
    filter_key: int
    column_value: int


class TableData:
    """テーブルデータ

    レコードのリストと主キーインデックスを保持。
    主キーによる高速な検索をサポート。
    """

    def __init__(self, capacity: int = 0) -> None:
        """初期化

        Args:
            capacity: 初期容量のヒント（最適化用）
        """
        self._records: List[TableRecord] = []
        self._pk_index: Dict[int, int] = {}  # primary_key -> list index

    def insert(self, record: TableRecord) -> None:
        """レコードを挿入

        Args:
            record: 挿入するレコード
        """
        idx = len(self._records)
        self._pk_index[record.primary_key] = idx
        self._records.append(record)

    def get_by_pk(self, pk: int) -> Optional[TableRecord]:
        """主キーでレコードを取得

        Args:
            pk: 主キー

        Returns:
            レコード、見つからない場合はNone
        """
        idx = self._pk_index.get(pk)
        return self._records[idx] if idx is not None else None

    def iter(self) -> Iterator[TableRecord]:
        """全レコードをイテレート

        フルスキャン用のイテレータを返す

        Returns:
            レコードのイテレータ
        """
        return iter(self._records)

    def __len__(self) -> int:
        """レコード数を取得

        Returns:
            レコード数
        """
        return len(self._records)


class IndexData:
    """Bツリーインデックスの簡易シミュレーション

    bisectモジュールを使用してBツリーのO(log n)検索特性をシミュレート。
    ソート済みキーリストと、キーから主キーリストへのマッピングを保持。
    """

    def __init__(self) -> None:
        """初期化"""
        # ソート済みキーリスト（Bツリーのソート特性をシミュレート）
        self._keys: List[int] = []
        # キー -> 主キーリストのマッピング
        self._index: Dict[int, List[int]] = {}

    def insert(self, filter_key: int, primary_key: int) -> None:
        """インデックスエントリを追加

        Args:
            filter_key: インデックスキー
            primary_key: 対応する主キー
        """
        if filter_key not in self._index:
            self._index[filter_key] = []
            # bisect.insort()でソート済み状態を維持（Bツリーのソート特性）
            bisect.insort(self._keys, filter_key)
        self._index[filter_key].append(primary_key)

    def search(self, filter_key: int) -> Optional[List[int]]:
        """インデックス検索（Bツリー探索をシミュレート）

        bisect.bisect_left()を使用してO(log n)の二分探索を実行。
        これによりBツリーの探索特性をシミュレート。

        Args:
            filter_key: 検索キー

        Returns:
            一致する主キーのリスト、見つからない場合はNone
        """
        # bisect.bisect_left()でO(log n)二分探索を実行
        pos = bisect.bisect_left(self._keys, filter_key)
        if pos < len(self._keys) and self._keys[pos] == filter_key:
            return self._index[filter_key]
        return None

    def __len__(self) -> int:
        """インデックスエントリの総数を取得

        Returns:
            全キーに対する主キーの総数
        """
        return sum(len(pks) for pks in self._index.values())
