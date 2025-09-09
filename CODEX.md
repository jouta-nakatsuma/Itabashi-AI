# CODEX メモ（Itabashi-AI 開発運用）

このドキュメントは、今後の自分（コデックス）の作業手順・運用方針・定型コマンドのメモです。

## 環境変数
- `.env.template` をコピーして `.env` を用意
  - `DB_URL=postgresql://user:pass@localhost:5432/itabashi_ai`
  - `OPENAI_API_KEY=`（必要に応じて設定）
  - `EMBEDDING_MODEL=text-embedding-3-small`
  - `DATA_PATH=./data/curated`

## Poetry（ローカル開発）
- 依存インストール: `poetry install`
- 実行例: `poetry run uvicorn mcp.server:app --reload`
- 型/リント/テスト: `poetry run mypy .` / `poetry run ruff check .` / `poetry run pytest`
- 依存追加: `poetry add <pkg>`（開発用は `--group dev`）
- ロック更新: `poetry lock`

## Docker / Compose
- 起動: `docker compose -f docker/docker-compose.yml up -d`
- 停止: `docker compose -f docker/docker-compose.yml down`
- ビルド（手動）: `docker build -f docker/Dockerfile -t ghcr.io/jouta-nakatsuma/itabashi-ai:latest .`
- ランログ/ヘルス: `curl localhost:8000/health`
- 備考: Dockerfile は `poetry lock` をビルド中に実行するため、ロックがなくてもビルド可

## GitHub Actions（CI/CD）
- トリガー: push / PR（main ではDocker Build & GHCR Push）
- 主要ジョブ:
  - Lint: Ruff
  - Type: mypy
  - Test: pytest（現状は雛形なので `|| true` で落とさない）
  - Docker: `ghcr.io/jouta-nakatsuma/itabashi-ai:latest` に Push
- 速度最適化（必要なら）:
  - `actions/cache` で Poetry キャッシュ追加検討

## ディレクトリ方針
- `mcp/`: FastAPI アプリ（`mcp.server:app`）と各種ツールの実装置き場
- `orchestrator/`: ルーティング、計画、出力レンダリング、安全性チェック
- `etl/`: データ取り込みとインデックス再構築（DB/ベクトル）
- `ui/`: UI 方針と試作（初期は Streamlit、将来的に Next.js）
- `data/`: 生成物・ローカルデータ（Git非追跡）
- `docker/`: Dockerfile / docker-compose.yml
- `mcp/config/`: topics/policy_map の雛形。運用時は要整備・拡張

## 次の実装候補
- MCP ツール実装
  - minutes: 会期/登壇者/会派/委員会での検索API
  - topics: `topics.yml` 読み込み → キーワード展開・関連議事録抽出
  - trends: 時系列出現頻度・移動平均・ピーク検出
  - policy: `policy_map.yml` によるカテゴリ→施策/部局マップ
  - geo: 地理参照・地区別集計
  - stats: 基礎統計・相関・簡易回帰
  - viz: 可視化（matplotlib/plotly）
  - report: Jinja2 レポート生成
- ETL
  - ingest_minutes: 公式サイト等の会議録収集→正規化→DB格納
  - ingest_opendata: CSV/JSON等をロード→スキーマ整備→DB
  - rebuild_index: 埋め込み生成→pgvector格納→メタ更新
- Orchestrator
  - router/planner/guards のスケルトンから簡易ルール実装
  - renderers: 表/グラフ/要約テンプレート
- UI
  - Streamlit ベースの簡易チャットUI試作

## 運用メモ
- ブランチ戦略: 当面は `main` 直push可。安定化後 `feat/*`→PR→CI→main へ
- バージョニング: リリースタグ `v0.x.y`、GHCRに同タグ push（将来）
- セキュリティ: `OPENAI_API_KEY` やDBパスワードは `.env` / GitHub Secrets 管理
- DB: ローカルは `docker-compose` の pgvector を利用。将来はマネージドDBへ

