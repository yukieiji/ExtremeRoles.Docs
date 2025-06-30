# ExtremeRoles.Doc
- ExtremeRoles.wikiをjust-the-docsによって作り替えたWiki

## Special Thanks
- ExtremeRoles.Docはこのテーマを使っています：https://github.com/just-the-docs/just-the-docs
- ExtremeRoles.Docはこのテンプレートを使用して作成しています：https://github.com/just-the-docs/just-the-docs-template

## 開発者向け情報

### テストの実行

このサイトには、Markdownファイルのフロントマターにおける `title` および `nav_order` の重複をチェックするテストが含まれています。テストはRubyで書かれています。

**前提条件:**

*   Ruby および Bundler がインストールされていること (Jekyllサイトの基本的な開発環境です)。
*   `bundle install` を実行して、必要なgem (jekyll, just-the-docs など) がインストールされていること。テストスクリプトに必要な `yaml` gemもこれにより通常解決されます。

テストを手動で実行するには、リポジトリのルートディレクトリで以下のコマンドを実行してください。

```bash
bundle exec rake test:site
```

### pre-commitフックによる自動チェック (推奨)

コミット前に自動的に上記のテストを実行するために、[pre-commit](https://pre-commit.com/) フレームワークを使用します。

**設定方法:**

1.  **pre-commitをインストールします。** (Python環境が必要です)
    お使いのシステムやプロジェクトのPython環境に応じて、以下のいずれかの方法でインストールしてください。

    ```bash
    # pipを使用する場合 (グローバルまたは仮想環境)
    pip install pre-commit
    ```
    または
    ```bash
    # Homebrew (macOS) を使用する場合
    brew install pre-commit
    ```
    他のインストール方法については、[pre-commitの公式ドキュメント](https://pre-commit.com/#install)を参照してください。

2.  **リポジトリにフックをインストールします。**
    リポジトリのルートディレクトリで以下のコマンドを実行してください。

    ```bash
    pre-commit install
    ```

これで、`git commit` を実行する際に、`.pre-commit-config.yaml` で定義されたチェックが自動的に実行されます。
チェックに失敗した場合、コミットは中止されます。エラーメッセージを確認し、問題を修正してから再度コミットしてください。

**フックを手動で実行する:**

特定のファイルや全てのファイルに対してフックを手動で実行することも可能です。

```bash
# ステージングされているファイルに対して実行
pre-commit run

# 全てのファイルに対して実行
pre-commit run --all-files
```