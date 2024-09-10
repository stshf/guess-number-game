# 数当てゲーム

このプロジェクトは、[Recursion](https://recursionist.io)というプログラミング学習サイトの課題として作成された、コマンドラインで遊べる数当てゲームです。ユーザーが指定した範囲内の乱数を生成し、その数を当てるゲームです。

## 課題の出典

この課題は、Recursionの以下のレッスンから出題されています：
[https://recursionist.io/dashboard/course/21/lesson/1084](https://recursionist.io/dashboard/course/21/lesson/1084)

## 機能

- ユーザーが最小値と最大値を設定
- 指定された回数以内に数を当てる
- 各推測に対してヒントを提供

## 必要条件

- Python 3.6以上
- Docker（オプション）

## 使用方法

### Pythonで直接実行

1. リポジトリをクローンします：
   ```
   git clone https://github.com/yourusername/guess-number-game.git
   cd guess-number-game
   ```

2. スクリプトを実行します：
   ```
   python guess_number.py
   ```

### Dockerで実行

1. Dockerイメージをビルドします：
   ```
   docker build -t guess-number-game .
   ```

2. コンテナを実行します：
   ```
   docker run -it guess-number-game
   ```

## 学習目標

このプロジェクトを通じて、以下のスキルを習得することを目指しています：

- Pythonの基本的な構文とロジックの理解
- ユーザー入力の処理とバリデーション
- 乱数の生成と使用
- 条件分岐とループの適切な使用
- Dockerを使用した環境のコンテナ化

## 貢献

このプロジェクトは学習目的で作成されていますが、改善の提案やバグ修正のプルリクエストは歓迎します。大きな変更を加える場合は、まずissueを開いて議論してください。

## ライセンス

このプロジェクトはRecursionの課題として作成されました。コードの使用や配布に関しては、Recursionの利用規約に従ってください。個人的な学習目的以外での使用は、事前にRecursionの許可を得る必要がある場合があります。

## 謝辞

このプロジェクトの課題を提供してくださった[Recursion](https://recursionist.io)に感謝いたします。

