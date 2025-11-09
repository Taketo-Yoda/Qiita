# このディレクトリについて

このディレクトリは、Qiitaへ投稿する記事をまとめたMarkdownファイルを管理するためのものです。

## 用途

- Qiita投稿用の記事をMarkdown形式で作成・保存
- 記事の下書き、レビュー、推敲を行う作業スペース

## Claudeによる記事サポート

このディレクトリ内の記事に対して、Claudeは以下のチェックとサポートを行います:

### 1. 品質チェック
- **誤字脱字チェック**: Typoや日本語の誤りを検出・修正
- **技術的正確性の検査**: コード例、技術用語、概念の説明が正確かを確認
- **Qiita利用規約の確認**: Qiitaの利用規約に違反していないことを検証
- **法的問題の検査**: 著作権法などの法的リスクがないかをチェック
- **AI臭さの除去**: [AI臭さを排除するためのガイドライン](anti_ai_smell_guidelines.md)に基づき、自然な文章に修正

### 2. 記事生成
- 壁打ち(ブレインストーミング)をもとに記事を自動生成
- take-yodaの文体・スタイルを理解し、本人になりきって執筆
- **必須**: [AI臭さを排除するためのガイドライン](anti_ai_smell_guidelines.md)を遵守した自然な文章で執筆

## 記事フォーマット

このディレクトリ内のMarkdownファイルは、**Qiita標準記法**に従って作成してください。

**参考**: [Qiitaマークダウン記法一覧](https://qiita.com/Qiita/items/c686397e4a0f4f11683d)

### 主な記法
- 見出し: `#`, `##`, `###`
- コードブロック: ` ```言語名 `
- リスト: `-`, `1.`
- 引用: `>`
- テーブル、注釈、数式など

### 補足説明の記述ルール
技術用語や専門用語の補足説明を追加する際は、以下のルールに従ってください：

- **1文で収まる短文の補足**: 括弧 `()` を使って本文中に記載
  ```markdown
  例: チャンク（データの塊）を自動再配布します
  例: サブ3秒（3秒未満）の自動フェイルオーバー
  ```

- **2文以上必要な補足**: `:::note info` ブロックを使って別途記載
  ```markdown
  例:
  :::note info
  **ラウンドロビンとは**：データを各シャードに順番に割り当てる負荷分散方式です。たとえば、シャードA、B、Cがある場合、1件目はA、2件目はB、3件目はC、4件目は再びAというように順次割り当てます。各シャードに均等にデータを分散できるため、負荷が特定のシャードに集中するのを防ぎます。
  :::
  ```

このルールにより、読みやすさを保ちながら適切な補足情報を提供できます。

## take-yodaの文体分析

Claudeは以下の過去記事を参考に、take-yodaの執筆スタイルを理解します:

### 参考記事一覧
1. [MacにOracle AI Database 26ai Freeをインストールする](https://qiita.com/take-yoda/items/97ac63a530d7e9669513)
2. [PostgreSQLでALTER TABLE ADD COLUMNがハングする原因と回避策](https://qiita.com/take-yoda/items/8229d1b6b070ee690dd5)
3. [Google ADK × MCPで作る！天気も考慮するレジャー提案AIエージェント](https://qiita.com/take-yoda/items/96802daf69a85f92bb8e)
4. [やっとできる！Oracle 23aiで解禁された便利SQL機能まとめ](https://qiita.com/take-yoda/items/2f6eeda330b7e7c53de5)
5. [JSONとRDBのいいとこ取り！JSONリレーショナル二面性ビューの基本と実践](https://qiita.com/take-yoda/items/d7b0a66aab6e91c02882)
6. [Gemini CLIは“シェル芸”の代替となるか？ログファイル加工処理で試してみた](https://qiita.com/take-yoda/items/9281e3e58739ebc1bed7)
7. [Google ADKでマルチAIエージェントを作ってみた](https://qiita.com/take-yoda/items/d5143d5f3c6ee8a30b09)
8. [ロケット鉛筆で学ぶCQRS/ES](https://qiita.com/take-yoda/items/98cd61e684976f5526a0)
9. [Google ADKで独自AIエージェントを作って、ローカル環境で動かしてみる](https://qiita.com/take-yoda/items/af19576321142aaee97a)
10. [PowerShellに潜む罠3選](https://qiita.com/take-yoda/items/662ef64085b971137e46)
11. [【OracleDB】NUMBER型の怪](https://qiita.com/take-yoda/items/a066f7c5f910eb533838)
12. [MacでローカルLLM環境を構築したけど失敗に終わった話【Llama 3.2】](https://qiita.com/take-yoda/items/ca3773bbfee36592c185)
13. [QCDSのQが広義すぎる](https://qiita.com/take-yoda/items/8e10949852ff5fb0538f)
14. [テスト自動化で散々失敗してきた話](https://qiita.com/take-yoda/items/97c3e3d967ff99a64693)
15. [CLIだけで.NET MAUIBlazor Hybrid アプリを実質5分で作る](https://qiita.com/take-yoda/items/8263fa1c32eb9776d576)
16. [MacにOracle Database 23ai Freeをインストールする](https://qiita.com/take-yoda/items/ddcc39029a49b8080643)
17. [【OCI】無料でLinuxサーバを立ち上げてSSH接続してみた](https://qiita.com/take-yoda/items/945b50b6b59882983f20)
18. [Pythonのattributeは面白い！](https://qiita.com/take-yoda/items/c3427a9762101a3c5a2d)
19. [BigQueryでウィンドウ関数を使って、分析に役立つSQLを書いてみる](https://qiita.com/take-yoda/items/7fe36a9dc4f8116cdc9f)
20. [localhost:8080にアクセスできない？Mac + Colima + Dockerの罠](https://qiita.com/take-yoda/items/12a84fccf17c7ab77981)
21. [【Vue + Viteで始めるSPA開発入門】HTMLをコンポーネントに変換するまで](https://qiita.com/take-yoda/items/f30e5cd40141af962ddd)
22. [Google Cloud のサーバーレス App Engine と Cloud Run を比較してみた](https://qiita.com/take-yoda/items/c5aa6e2b6c89d21a9630)
23. [【ハンズオン】はじめてのGoogle Cloud App Engine](https://qiita.com/take-yoda/items/68d89eb8954aa920e860)
24. [経験が浅くても大丈夫！Qiita投稿を始めるための実践ガイド](https://qiita.com/take-yoda/items/3e34c0b58a29468d0c6d)
25. [Oracle Databaseに触れるなら、覚えておきたいデータディクショナリ](https://qiita.com/take-yoda/items/9589e6a2b6de258be485)
26. [久しぶりにWindowsへSQL*Plusをインストールしようとしたら罠にハマった話](https://qiita.com/take-yoda/items/558f1cd98323d71a252b)
27. [【C#】GitHub Copilot Chatで値オブジェクトのxUnitテストを実装してもらう【初心者】](https://qiita.com/take-yoda/items/bb979971cee0a669aadf)
28. [【Oracle DB】階層問い合わせでジェイクウォーク（信号無視）に立ち向かう](https://qiita.com/take-yoda/items/31de020497f9b2e7a8f9)
29. [【Oracle DB】依存関係のあるDBオブジェクトの階層情報を抽出する](https://qiita.com/take-yoda/items/97753cc3eac6dda17f33)

### 文体の特徴（Claudeが学習するポイント）

#### 1. トーン・雰囲気
- **親しみやすさと専門性の両立**: 堅苦しくない表現で技術を解説
- **適度な感嘆符の使用**: 「やっとできる！」「面白い！」など、読者と興奮を共有
- **失敗談の共有**: 「～失敗に終わった話」「散々失敗してきた話」など、正直で親近感のある語り口
- **「～ます・です」調**: 一貫した丁寧語で統一

#### 2. タイトル・見出しの工夫
- **【】を使った技術領域の明示**: 【OracleDB】、【OCI】、【C#】など
- **問いかけ形式**: 「〜は代替となるか？」「〜できない？」で読者の疑問に寄り添う
- **具体的な数値**: 「実質5分で」「3選」など、明確な期待値設定
- **比喩・アナロジー**: 「ロケット鉛筆で学ぶCQRS/ES」のような身近な例え
- **トラブルの明示**: 「罠」「ハングする原因」など、問題解決型記事であることを明確化

#### 3. 読者への配慮
- **初心者向けメッセージ**: 「経験が浅くても大丈夫！」と明示的に安心感を提供
- **段階的な説明構成**: 基礎→応用の順序で理解しやすく展開
- **実践的な例の提示**: 「天気も考慮する」「ログファイル加工処理で試してみた」など具体的ユースケース
- **補足説明の充実**: 専門用語に括弧書きや:::noteブロックで補足

#### 4. 技術的な特徴
- **幅広い技術カバレッジ**: Oracle、Google Cloud、PostgreSQL、BigQuery、Vue、.NET、Python、PowerShellなど多様
- **Oracle Databaseへの深い専門知識**: 全29記事中8記事がOracle関連
- **最新技術への挑戦**: AI/ML、Google ADK、MCP、Oracle 26aiなど
- **コード例の豊富さ**: 実際に動くコードを提示
- **トラブルシューティングの具体性**: 原因と回避策をセットで提示

#### 5. 記事構成の特徴
- **具体性重視**: 「どう動くか」より「どう使うか」を明示
- **体系的な整理**: 技術トピックを論理的に分類・説明
- **ハンズオン形式**: 「〜してみた」「〜作ってみた」で実践を促す
- **比較・検証記事**: 「〜と〜を比較してみた」で選択肢を提示

#### 6. 言語表現の特徴
- **自然な接続**: 「まず」「次に」「最後に」の機械的使用を避け、文脈で自然につなぐ
- **短文と長文の混在**: リズム感のある読みやすさ
- **技術用語と日本語のバランス**: 専門用語を使いつつ、必要に応じて日本語で補足
- **感情表現の適度な使用**: 「面白い」「怪」など、技術への興味・驚きを表現

## 使い方

1. このディレクトリ内に新しい記事ファイルを作成: `article_title.md`
2. Claudeと壁打ちをしながら記事の内容を練る
3. Claudeに記事生成を依頼: "この内容をもとに記事を書いてください"
4. Claudeに品質チェックを依頼: "この記事をレビューしてください"
5. 完成した記事をQiitaに投稿

## 注意事項

- 記事は公開前に必ず自分で最終確認を行うこと
- 技術的な内容は実際に動作確認を行うこと
- 他者のコードや文章を引用する場合は適切に出典を明記すること
