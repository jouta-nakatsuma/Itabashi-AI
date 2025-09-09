"""MCP サーバ（FastAPI）。

役割:
- ヘルスチェック等の基本エンドポイント
- 将来的にMCPツールへのルーティングやOpenAI/MCPプロトコル実装の受け口
"""

from fastapi import FastAPI
import os

app = FastAPI(title="Itabashi AI MCP Server")


@app.get("/health")
def health() -> dict:
    """簡易ヘルスチェック。

    DB_URLが環境変数に設定されているかも合わせて返す。
    """
    return {
        "status": "ok",
        "db_url": bool(os.getenv("DB_URL")),
    }

