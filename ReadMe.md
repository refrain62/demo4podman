# VS Code から Podman コンテナ@Mac＆Windows にDevContainerを使って接続＆開発
https://qiita.com/trtrbohz/items/4ee2a8db1aa7177e40a5 の写経

## VSCの設定
「Docker」拡張 に関して「拡張機能の設定」から Podman のコマンドパスを指定します。
① 「Docekr」拡張の右にある歯車アイコンをクリックし、メニューの中から「拡張機能の設定」を選択
② 上記検索ウィンドウに「DockerPath」を入力
③ 「Dev 〉 Docker:Docker Path」を下図のように「docker」→「podman」

## イメージ作成とコンテナ実行
ビルド
```
$ podman build -f ./Dockerfile -t flaskapp:latest .
```

イメージからコンテナを実行
```
$ podman run --name vscodeTestFlask -t -v ./app:/app -p 9000:80 -d localhost/flaskapp
```

http://localhost:9000 にアクセス


## コンテナの共有フォルダを使って新規アプリ開発
