# AI分析への進展

**User:** Anonymous (sunpin32@yahoo.co.jp)  
**Created:** 9/10/2025 0:02:01  
**Updated:** 9/10/2025 1:29:18  
**Exported:** 9/10/2025 1:30:00  
**Link:** [https://chatgpt.com/g/g-p-68a2428917408191ab595311b37e4516-itabashi-minutes/c/68c04167-6a24-832a-a158-b4f86eb7e895](https://chatgpt.com/g/g-p-68a2428917408191ab595311b37e4516-itabashi-minutes/c/68c04167-6a24-832a-a158-b4f86eb7e895)  

## Response:
了解しました ✨  
では、**Dockerビルド & イメージPush（GitHub Container Registry前提）** を最初から含めた、完全版の初期化プロンプトを提示します。

* * *

📜 コデックス指示プロンプト（Poetry + CI/CD + Docker Push 完全版）
-------------------------------------------------

```
リポジトリ: Itabashi-AI

目的:
「Itabashi AI」は、板橋区議会会議録や区オープンデータをバックエンドDBに格納し、
MCPサーバを通じてAIオーケストレーションを行い、
ChatGPT/NotebookLM風のUIから知識を自在に呼び出せるシステムである。

やること:
リポジトリ初期化。以下のディレクトリ構成とファイルを生成すること。

ディレクトリ構成:
Itabashi-AI/
  README.md
  .gitignore
  .env.template
  pyproject.toml
  poetry.lock        # 空ファイル（Poetry実行で生成される想定）
  mcp/
    __init__.py
    server.py
    tools/
      __init__.py
      minutes.py
      topics.py
      trends.py
      policy.py
      geo.py
      stats.py
      viz.py
      report.py
    config/
      topics.yml
      policy_map.yml
  orchestrator/
    __init__.py
    router.py
    planner.py
    renderers.py
    guards.py
  ui/
    README.md   # UIの方向性説明（Next.js or Streamlitチャット）
  etl/
    ingest_minutes.py
    ingest_opendata.py
    rebuild_index.py
  data/
    .gitkeep
  docker/
    Dockerfile
    docker-compose.yml
  .github/
    workflows/
      ci.yml

ファイル要件:
- README.md: プロジェクト概要（目的・構造・今後の方向性を記述）
- .gitignore: 以下を必ず含める
    - Mac固有: `.DS_Store`
    - Python: `__pycache__/`, `.venv/`, `*.pyc`, `*.pyo`, `.mypy_cache/`, `.pytest_cache/`, `.ruff_cache/`
    - Node: `node_modules/`, `npm-debug.log*`, `yarn-debug.log*`, `yarn-error.log*`
    - Docker: `/dist`, `/build`, `*.log`
- .env.template: 環境変数の雛形
    - `DB_URL=postgresql://user:pass@localhost:5432/itabashi_ai`
    - `OPENAI_API_KEY=`
    - `EMBEDDING_MODEL=text-embedding-3-small`
    - `DATA_PATH=./data/curated`
- pyproject.toml: Poetry 初期化ファイル
    - `[tool.poetry]` name="itabashi-ai"
    - version="0.1.0"
    - description="Itabashi AI: Knowledge OS for Itabashi Ward"
    - authors=["Jouta Nakatsuma <your_email@example.com>"]
    - python="^3.13"
    - 依存パッケージ（初期セット）:
        - fastapi
        - uvicorn
        - psycopg[binary]
        - pgvector
        - pandas
        - duckdb
        - pyyaml
        - openai
        - python-dotenv
        - httpx
        - jinja2
        - rich
        - typer
    - dev依存パッケージ:
        - pytest
        - ruff
        - mypy
- docker-compose.yml:
    - サービス: postgres(pgvector拡張込み), mcp-server(FastAPI), adminer(任意)
    - MCPサーバは .env からDB_URLを受け取り起動
- Dockerfile:
    - ベース: python:3.13-slim
    - Poetryインストール
    - `poetry install --no-root`
    - uvicornで `mcp.server:app` を起動するENTRYPOINT
- .github/workflows/ci.yml:
    - トリガー: push / pull_request
    - ジョブ内容:
        1. Python 3.13 セットアップ
        2. Poetry セットアップ & キャッシュ
        3. 依存インストール
        4. Lint（ruff）
        5. 型チェック（mypy）
        6. テスト（pytest）
        7. Docker Build & Push (mainブランチのみ)
            - イメージ名: `ghcr.io/jouta-nakatsuma/itabashi-ai:latest`
            - GitHub Container Registry を利用
            - `GITHUB_TOKEN` を利用してpush

注意点:
- 各Pythonファイルは空でよいが、docstringで役割を明記すること
- topics.yml / policy_map.yml はコメント付きの雛形にすること
- CI/CDはLint+Testに加え、mainブランチではDockerイメージを自動Build & Pushすること
- diffや抜粋ではなく、リポジトリ全体の初期ファイルをフル生成すること
```

* * *

これで初期から **Poetry + CI/CD + Docker Build/Push** まで自動化されたリポジトリになります 🚀

👉 穣太さん、このDockerイメージのPush先は `ghcr.io/jouta-nakatsuma/itabashi-ai` でよいですか？（GitHub Container Registryを前提にしましたが、Docker Hubなど別Registryにしますか？）



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)