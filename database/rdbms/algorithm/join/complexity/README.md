# RDBMS Join Algorithm Complexity Simulator

RDBMSのテーブル結合アルゴリズム（Nested Loop JoinとHash Join）をシミュレーションし、実行時間とBig-O計算量を可視化するCLIツールです。

## 概要

このツールは、RDBMSにおける2つの主要な結合アルゴリズムの性能特性を実データで検証できます：

- **Nested Loop Join**: 駆動表の各行に対して外部表を検索
- **Hash Join**: ハッシュテーブルを構築してプローブ

インデックスの有無による性能差を実測値とBig-O表記の両方で確認できます。

## 機能

- ✅ 実データを生成してJOIN処理を実行
- ✅ 実際の処理時間を計測（マイクロ秒精度）
- ✅ Big-O計算量を理論値と実測値で表示
- ✅ インデックス使用/未使用の比較
- ✅ テーブルアクセス回数の可視化
- ✅ BTreeMapによるB-treeインデックスのシミュレーション

## インストール

### 前提条件

- Rust 1.70以上

### ビルド

```bash
cd database/rdbms/algorithm/join/complexity
cargo build --release
```

## 使い方

### 基本構文

```bash
cargo run --release -- [OPTIONS]
```

または、ビルド後のバイナリを直接実行：

```bash
./target/release/join-sim [OPTIONS]
```

### オプション

| オプション | 短縮形 | 説明 | 必須 |
|-----------|--------|------|------|
| `--inner-total` | `-a` | 駆動表の母数（万件） | ✓ |
| `--fetch-ratio` | `-b` | fetchする件数の比率（%、1-100） | ✓ |
| `--inner-use-index` | - | 駆動表でインデックスを使用 | - |
| `--join-algorithm` | `-j` | 結合アルゴリズム（`nl` または `hash`） | ✓ |
| `--outer-total` | `-c` | 外部表の母数（万件） | ✓ |
| `--join-factor` | `-d` | 駆動表1レコードあたりの結合件数（≥1） | ✓ |
| `--outer-use-index` | - | 外部表でインデックスを使用（`nl`時のみ） | - |
| `--filter-value` | - | フィルタ条件の値（デフォルト: 20） | - |

### 制約条件

- `a × 10,000 × d ≤ c × 10,000` を満たす必要があります
- `b` は 0 < b ≤ 100 の範囲
- `d` は 1 以上の整数

## 実行例

### 1. Nested Loop Join - 両方インデックス使用（最適ケース）

```bash
cargo run --release -- \
  -a 10 -b 50 --inner-use-index \
  -j nl -c 100 -d 5 --outer-use-index
```

**期待される出力:**
```
=== RDBMS Join Algorithm Simulator ===
Inner table: 100000 records
Fetch ratio: 50%
Inner index: true
Join algorithm: NestedLoop
Outer table: 1000000 records
Join factor: 5
Outer index: true

Generating test data...
Data generation completed.

Executing join...

=== Results ===
Algorithm: Nested Loop Join
Execution time: 125.456ms
Inner table accesses: 1
Outer table accesses: 250000
Result count: 250000

=== Complexity Analysis ===
Nested Loop Join (両方インデックス使用)
Inner scan: O(log n + m) = O(log 100000 + 50000) ≈ 1
Outer scan: O(m * (log c + d)) = O(50000 * (log 1000000 + 5)) ≈ 250000
Total: O(m * log c) where m=50000, c=1000000
```

### 2. Hash Join - 駆動表のみインデックス使用

```bash
cargo run --release -- \
  -a 5 -b 80 --inner-use-index \
  -j hash -c 50 -d 3
```

**期待される特性:**
- Build Phase: O(m)
- Probe Phase: O(c)
- Total: O(m + c)

Hash Joinは外部表のインデックスを使用せず、常にFull Scanします。

### 3. Nested Loop Join - インデックス未使用（最悪ケース）

```bash
cargo run --release -- \
  -a 2 -b 100 \
  -j nl -c 20 -d 2
```

**期待される特性:**
- Inner scan: O(n)
- Outer scan: O(m * c)
- 最も遅い実行時間

### 4. 小規模データでのクイックテスト

```bash
cargo run --release -- \
  -a 1 -b 50 --inner-use-index \
  -j nl -c 10 -d 5 --outer-use-index
```

## データモデル

### テーブル構造

各テーブルは以下のフィールドを持ちます：

```rust
struct TableRecord {
    primary_key: u64,      // 主キー
    filter_key: u64,       // WHERE条件で使用
    column_value: u64,     // JOIN条件で使用
}
```

### SQL相当の処理

シミュレートしているSQLは以下のイメージです：

```sql
SELECT b.column_value
FROM inner_table a
INNER JOIN outer_table b
  ON a.column_value = b.filter_key
WHERE a.filter_key = 20
```

### インデックス構造

- **IndexData**: `BTreeMap<u64, Vec<u64>>` を使用
  - filter_key → primary_keys のマッピング
  - B-treeによるソート済みインデックスを実現

## アルゴリズムの計算量

### Nested Loop Join

| ケース | 駆動表 | 外部表 | 計算量 |
|--------|--------|--------|--------|
| 両方インデックス | O(log n + m) | O(m × log c) | **O(m × log c)** |
| 駆動表のみ | O(log n + m) | O(m × c) | **O(m × c)** |
| 外部表のみ | O(n) | O(m × log c) | **O(n + m × log c)** |
| 両方未使用 | O(n) | O(m × c) | **O(m × c)** |

### Hash Join

| ケース | 駆動表 | Build | Probe | 計算量 |
|--------|--------|-------|-------|--------|
| インデックス使用 | O(log n + m) | O(m) | O(c) | **O(m + c)** |
| インデックス未使用 | O(n) | O(m) | O(c) | **O(n + m + c)** |

**記号の意味:**
- `n`: 駆動表の総レコード数
- `m`: 駆動表のfetch件数（n × fetch_ratio / 100）
- `c`: 外部表の総レコード数

## プロジェクト構造

```
database/rdbms/algorithm/join/complexity/
├── Cargo.toml
├── README.md
├── src/
│   ├── main.rs              # メインエントリーポイント
│   ├── cli.rs               # CLI引数パース
│   ├── data/
│   │   ├── mod.rs
│   │   ├── table.rs         # TableData/IndexData構造体
│   │   └── generator.rs     # テストデータ生成
│   ├── join/
│   │   ├── mod.rs
│   │   ├── traits.rs        # JoinAlgorithmトレイト
│   │   ├── nested_loop.rs   # Nested Loop Join実装
│   │   └── hash_join.rs     # Hash Join実装
│   └── metrics/
│       ├── mod.rs
│       └── complexity.rs    # Big-O計算量算出
```

## パフォーマンス最適化

リリースビルドで実行することを推奨します：

```bash
cargo run --release -- [OPTIONS]
```

リリースビルドでは以下の最適化が有効になります：
- `opt-level = 3`: 最高レベルの最適化
- `lto = true`: Link Time Optimization

## ヘルプ

詳細なヘルプを表示：

```bash
cargo run --release -- --help
```

## トラブルシューティング

### エラー: "Constraint violation: a * 10000 * d (X) > c * 10000 (Y)"

外部表のレコード数が不足しています。`-c`（外部表の母数）を増やしてください。

**制約:** `a × 10,000 × d ≤ c × 10,000`

### エラー: "Percentage must be between 0 and 100"

`-b`（fetch比率）は 0 < b ≤ 100 の範囲で指定してください。

### 警告: "Warning: --outer-use-index is ignored for Hash Join"

Hash Joinでは外部表のインデックスは使用されません。この警告は無視して問題ありません。

## ライセンス

このプロジェクトは学習・研究目的で作成されています。

## 参考文献

- RDBMSの結合アルゴリズム
- B-treeインデックス構造
- データベースクエリ最適化
