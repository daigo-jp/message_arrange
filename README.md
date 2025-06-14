# Message_arrange                                      

## 概要
送信したメッセージをビジネスシーンで使える丁寧な言葉に変換してくれる

## 主な機能
- Home画面
<img src="screenshots/home.png" alt="Home画面" width="400">
- メッセージ送信
<img src="screenshots/msg.png" alt="メッセージ送信" width="400">
- メッセージ履歴
<img src="screenshots/msg_history.png" alt="履歴" width="400">

## 使用技術

- Python / Django（バックエンド）
- SQLite（データベース）
- HTML / CSS（フロントエンド）

##苦労、工夫した点

- 初めてAPIを活用したので利用規約などをきちんと読んだ
- APIを使用するための流れをつかむのが大変だった

## AI活用について  
開発にあたって、AIを活用して以下の支援を受けました。

- CSSなどのレイアウト
- エラーの原因特定と解決方法の提案  

## 起動方法（開発環境）
```bash
git clone https://github.com/daigo-jp/message_arrange
cd myproject
python manage.py migrate
python manage.py runserver
