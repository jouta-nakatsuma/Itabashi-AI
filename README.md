# Itabashi AI

Itabashi AI は、板橋区議会の会議録や区オープンデータ等をバックエンドDBに格納し、MCPサーバを通じてAIオーケストレーションを行い、ChatGPT/NotebookLM風UIから知識を自在に呼び出せるシステムです。

## 目的
- 会議録・オープンデータの統合的インジェストと索引構築
- MCPツール群による推論・検索・可視化のオーケストレーション
- 使いやすい対話型UIによる情報探索とレポート生成

## ディレクトリ構成
- `mcp/`: MCPサーバ（FastAPI）とツール群
- `orchestrator/`: ルーティング、プランナー、レンダラー、ガード
- `etl/`: データ取り込み・前処理・インデックス再構築
- `ui/`: UIの方針メモ（Next.js または Streamlit）
- `docker/`: Dockerfile と docker-compose
- `data/`: ローカルデータ配置（Git管理外）

## クイックスタート
1. `.env.template` を `.env` にコピーして必要値を設定
2. Poetryで依存を用意: `poetry install`
3. Docker Composeで起動: `docker compose -f docker/docker-compose.yml up -d`

## 今後の方針
- トピック/トレンド/政策マップ/地理/統計/可視化/レポートの各MCPツール拡充
- RAGやキャッシュを活用した高速応答
- UIのプロトタイプ（Next.js または Streamlit）

## ライセンス
TBD

