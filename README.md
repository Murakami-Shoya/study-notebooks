# study-notebooks

個人学習用Notebookリポジトリ（1教材1notebook）

BCI / ECoG音声デコード研究に関連する論文・教材を1つのノートブックにまとめ，手を動かして理解を深めるためのリポジトリ．

## ディレクトリ構成

```
.
├── notebooks/           # 各教材のノートブック
│   ├── YYYY-MM-DD_<topic-slug>.ipynb          # 単一教材（サブページなし）
│   └── <topic-slug>/                          # 複数ページ教材（Notionにサブページあり）
│       ├── 00_overview.ipynb                  # 概要
│       ├── 01_<subpage-name>.ipynb           # サブページ1
│       └── 02_<subpage-name>.ipynb           # サブページ2（ページ順に番号付け）
├── src/                # 共有ユーティリティ（必要に応じて追加）
├── templates/          # テンプレートノートブック
├── .github/workflows/  # CI（全notebookの実行テスト）
└── pyproject.toml      # Python環境定義
```

## 環境セットアップ

### uv（推奨）

```bash
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -e .
```

### pip

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
```

### オプション依存関係

```bash
# PyTorch（深層学習の教材で必要な場合）
uv pip install -e ".[torch]"

# nbstripout（notebook出力を自動削除，オプション）
uv pip install -e ".[dev]"
nbstripout --install  # Git hookを設定
```

### Jupyter起動

```bash
jupyter notebook
```

## 新しい教材の追加方法

1. **テンプレートをコピー**
   ```bash
   # Notionページにサブページがない場合（単一ノートブック）
   cp templates/material_template.ipynb notebooks/YYYY-MM-DD_<topic-slug>.ipynb
   
   # Notionページにサブページがある場合（フォルダ構成）
   mkdir notebooks/<topic-slug>
   cp templates/material_template.ipynb notebooks/<topic-slug>/00_overview.ipynb
   # サブページごとにコピー・番号付け
   ```

2. **ファイル名規則**
   - **単一教材**: `YYYY-MM-DD_<short-topic-slug>.ipynb`
   - **複数ページ教材**: `<topic-slug>/NN_<subpage-name>.ipynb`（`00_overview.ipynb`から開始）
   - 例: `2026-10-20_group-lasso.ipynb`, `transformer/00_overview.ipynb`, `transformer/01_attention.ipynb`
   - 日付は学習開始日（単一教材のみ）
   - slugは英小文字・ハイフン区切り，簡潔に

3. **ノートブック記入**
   - 冒頭に「Open in Colab」バッジを追加（URLはファイルパスに合わせて修正）
   - タイトル・出典（Notion教材ページURL）
   - **Notionとの役割分担**: Notionページに理論・数式・直感・用語解説を記載し，ノートブックはコードで主張を検証するのみ
   - **シナリオ構成**: シナリオ一覧テーブル（# | シナリオ | 確かめること | 期待する結果 | 解説の節）を冒頭に配置
   - **準備セクション**: データ生成・ヘルパー関数をまとめて冒頭に定義
   - **各シナリオ**: `## S1. ...` の見出し，1-2行の説明，15行以内のコードセル（1セル1アイデア），図または数値，観察（assertで検証）
   - **図のテキスト**: タイトル・軸・凡例・注釈はすべて英語（日本語はmarkdownセルのみ）
   - **まとめ**: 3行以内
   - **サイズ目安**: 全体で~20-25セル，~150行のコード，CPU完結，実行1分未満
   - **Colab対応**: 最初のコードセルでColab用セットアップを実行（テンプレート参照）

4. **下記の索引テーブルに追記**（Colabバッジ付き）

5. **動作確認**
   ```bash
   jupyter nbconvert --to notebook --execute notebooks/YYYY-MM-DD_<topic-slug>.ipynb
   ```

## 教材索引

| 日付 | 教材 | Notebook | Colab | Notion |
|------|------|----------|-------|--------|
| 2026-10-20 | スパースモデリングとグループラッソ入門 | [📓](notebooks/2026-10-20_group-lasso.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Murakami-Shoya/study-notebooks/blob/main/notebooks/2026-10-20_group-lasso.ipynb) | [🧵](https://app.notion.com/p/3f43834a206d81d98a78c761f713daea) |

## Google Colab での実行

各ノートブックは Google Colab で直接実行できます．

- **セットアップ**: 各ノートブックの最初のコードセルがColab環境を自動検出し，不足パッケージをインストールします．
- 上記の索引テーブルのColabバッジをクリックすると直接開きます．

## ノートブック出力の管理（オプション）

Notebookの出力（図・実行結果）はGitで追跡すると差分が大きくなるため，以下のいずれかを推奨：

- **手動**: コミット前に `Kernel > Restart & Clear Output` で出力をクリア
- **自動（nbstripout）**: `uv pip install -e ".[dev]" && nbstripout --install` で自動削除

## CI

`.github/workflows/test-notebooks.yml` が全notebookを自動実行し，エラーを検出します．
Notebookは小規模な合成データでCPU上で完結するように作成してください．
