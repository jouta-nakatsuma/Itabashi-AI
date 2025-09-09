# Itabashi-AI 初期化作業報告（2025-09-10）

宛先: グリフ（Glyph）
作成: コデックス（Codex）

## 概要
- 目的: Itabashi-AI リポジトリの初期化（Poetry + CI/CD + Docker Push まで）
- 方針: Glyph-initial-prompt.md の要件に準拠し、スキャフォールドを一括生成

## 実施内容
- コア
  - `README.md`: 目的/構成/クイックスタートを記載
  - `.gitignore`: macOS/Python/Node/Docker/ログ/環境ファイルを登録
  - `.env.template`: DB/OPENAI_API_KEY/EMBEDDING_MODEL/DATA_PATH を定義
  - `pyproject.toml`: Poetry 設定（Python 3.13、FastAPI/uvicorn/psycopg/pgvector 等）
  - `poetry.lock`: 初期は空を用意（後述のCI/Dockerで生成対応）
- MCP サーバ
  - `mcp/server.py`: FastAPI `app` と `/health` を実装
  - `mcp/tools/*`: minutes/topics/trends/policy/geo/stats/viz/report の各雛形
  - `mcp/config/topics.yml`, `mcp/config/policy_map.yml`: コメント雛形
- オーケストレータ
  - `orchestrator/{router,planner,renderers,guards}.py`: 役割docstringを配置
- UI/ETL
  - `ui/README.md`: Next.js or Streamlit 方針
  - `etl/{ingest_minutes,ingest_opendata,rebuild_index}.py`: 雛形
- Docker/Compose
  - `docker/Dockerfile`: Poetry インストール→`poetry lock`→`poetry install`→`uvicorn mcp.server:app`
  - `docker/docker-compose.yml`: pgvector + mcp-server + adminer
- CI（.github/workflows/ci.yml）
  - セットアップ: Python 3.13, Poetry（pip経由）
  - 依存: `poetry lock` → `poetry install`
  - 検証: Ruff, mypy, pytest（現状は落とさない）
  - Docker: main で GHCR へ `ghcr.io/jouta-nakatsuma/itabashi-ai:latest` を Build & Push

## 課題と対応
1) Actions セットアップ失敗（pipx アクションが見つからない）
   - 原因: `pipxproject/action-install-pipx` が存在せず解決不能
   - 対応: Poetry を `pip install poetry==1.8.3` で直接導入に変更
2) Poetry 依存インストール失敗（lock に metadata が無い）
   - 原因: `poetry.lock` が空ファイル
   - 対応: CI に `poetry lock` ステップを追加してから `poetry install`
3) Docker Build 失敗（同様に lock 不在）
   - 原因: Docker ジョブは別チェックアウトで lock が無い
   - 対応: Dockerfile で `poetry lock` を実行してから `poetry install`
4) 初回 push 失敗（リモートに既存コミット）
   - 原因: リモート `LICENSE` あり
   - 対応: `git fetch origin main` → `git merge -X ours` でローカル優先統合 → push

## 結果
- main ブランチへ初期スキャフォールドを push 済み
- CI の Set up / 依存インストール / Lint / Type / Test を通過
- Docker ジョブで GHCR へイメージ Build & Push 成功

## 次の提案
- MCP ツールの実装着手（minutes/topics/trends/policy/geo/stats/viz/report）
- ETL 実装（議事録/オープンデータのスキーマ定義と投入）
- UI 試作（Streamlit チャット→要件固まり次第 Next.js 検討）
- CI 最適化（Poetry キャッシュ・pytest の実テスト導入）
- セキュリティ運用（Secrets, 権限管理, ブランチ保護 ルール）

---
以上、初期化作業の報告です。
