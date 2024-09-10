# Ubuntu 最新版をベースイメージとして使用
FROM ubuntu:latest

# 環境変数を設定してインタラクティブモードを無効化
ENV DEBIAN_FRONTEND=noninteractive

# パッケージリストを更新し、必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Python3をデフォルトのpythonとして設定
RUN ln -s /usr/bin/python3 /usr/bin/python

# 作業ディレクトリを設定
WORKDIR /app

# ソースコードをコピー
COPY src/ .

# requirements.txtをコピー（空でも問題ありません）
COPY requirements.txt .

# 必要なパッケージをインストール
RUN if [ -s requirements.txt ]; then pip3 install --no-cache-dir -r requirements.txt; fi

# Pythonのバッファリングを無効にして、ログをリアルタイムで表示
ENV PYTHONUNBUFFERED=1

# コンテナ起動時にゲームを実行
CMD ["python3", "guess_number.py"]