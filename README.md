# scrapingpy template

BeautifulSoup4を使ってPythonでスクレイピングを実施するテンプレートプロジェクトです。
次の処理を試しながらBeautifulSoupの基本を学習できます。

1. Webページのタイトルを取得する。
2. 要素をひとつ取得する。
3. 複数の要素をを取得する。
4. 要素の属性を取得する。
5. 子要素を取得する。
6. 【応用】JavaScriptが処理された後の要素を取得する。


```フォルダ構成
.
├── README.md
├── scraping            # projectファイル
│       └── main.py    # discordpyスクリプト
├── html                # スクレイピング対象のサンプルHTMLファイル一式
├── .devcontainer       # Docker Remote Container用ファイル一式
├── docker-compose      # Docker Compose用ファイル
├── poetry.lock         # poetry依存関係
└── pyproject.toml      # pythonプロジェクトにおける開発設定ファイル
```

## 使用言語
* python

## ライブラリ
* beautifulsoup4
* selene
* requests
* isort
* black
* flake8

## 開発ツール
* vscode
* github codespace または remote conteiner(docker)
