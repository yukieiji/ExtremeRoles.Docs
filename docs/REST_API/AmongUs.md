---
layout: default
title: AmongUs API
parent: REST API
nav_order: 1
---

# AmongUs API

- AmongUs本体に存在している各種情報にアクセスするためのAPI郡

## チャット履歴の取得(表示されている部分すべて)
- GET : http://localhost:57700/au/chat/

| ステータスコード | 説明 |
| --- | --- |
| 200 | OK |

- レスポンススキーマ
```json
{
  "type": "object",
  "properties": {
    "IsMeeting" : {
      "type": "bool",
    },
    "AllChat" : [
      "type": "array",
      "Items": {
        "titele": "Chat Info",
        "description": "One Chat Infos",
        "type": "object",
        "properties": {
          "Sender": {
            "description": "Chat Sender",
            "type": "object",
            "properties": {
              "PlayerName" : {
                "description": "Player Name Info",
                "type": "object",
                "properties": {
                  "PlayerName" : {
                    "description": "PlayerName",
                    "type": "string",
                    "examples": [
                      "yukieiji"
                    ]
                  },
                  "ShowColor" : {
                    "description": "PlayerName Text Color",
                    "type": "object",
                    "properties": {
                      "RGBA" : {
                        "type" : "int"
                      },
                      "R" : {
                        "description": "Color R Value",
                        "type" : "byte"
                      },
                      "G" : {
                        "description": "Color G Value",
                        "type" : "byte"
                      },
                      "B" : {
                        "description": "Color B Value",
                        "type" : "byte"
                      },
                      "A" : {
                        "description": "Color Alpha Value",
                        "type" : "byte"
                      }
                    }
                  }
                }
              },
              "CosmicInfo" : {
                "description": "Player Cosmic Info",
                "type": "object",
                "properties": {
                  "Color" : {
                    "description": "Player Color Info",
                    "type": "object",
                    "properties": {
                      "ColorId" : {
                        "description": "AmongUs Color Id",
                        "type" : "int"
                      },
                      "ColorNameId" : {
                        "description": "AmongUs Color Name Id(used by translations)",
                        "type" : "int"
                      },
                      "MainColor" : {
                        "description": "Player Body Main Color",
                        "type": "object",
                        "properties": {
                          "RGBA" : {
                            "type" : "int"
                          },
                          "R" : {
                            "description": "Color R Value",
                            "type" : "byte"
                          },
                          "G" : {
                            "description": "Color G Value",
                            "type" : "byte"
                          },
                          "B" : {
                            "description": "Color B Value",
                            "type" : "byte"
                          },
                          "A" : {
                            "description": "Color Alpha Value",
                            "type" : "byte"
                          }
                        }
                      },
                      "ShadowColor" : {
                        "description": "Player Body Shadow Color",
                        "type": "object",
                        "properties": {
                          "RGBA" : {
                            "type" : "int"
                          },
                          "R" : {
                            "description": "Color R Value",
                            "type" : "byte"
                          },
                          "G" : {
                            "description": "Color G Value",
                            "type" : "byte"
                          },
                          "B" : {
                            "description": "Color B Value",
                            "type" : "byte"
                          },
                          "A" : {
                            "description": "Color Alpha Value",
                            "type" : "byte"
                          }
                        }
                      }
                    }
                  },
                  "HatId" : {
                    "description": "AmongUs Hat Id",
                    "type": "string",
                    "examples": [
                      "yukieiji_test_hat"
                    ]
                  },
                  "VisorId" : {
                    "description": "AmongUs visor Id",
                    "type": "string",
                    "examples": [
                      "yukieiji_test_visor"
                    ]
                  },
                  "SkinId" : {
                    "description": "AmongUs Skin Id",
                    "type": "string",
                    "examples": [
                      "yukieiji_test_skin"
                    ]
                  },
                  "PetId" : {
                    "description": "AmongUs Pet Id",
                    "type": "string",
                    "examples": [
                      "yukieiji_test_pet"
                    ]
                  },
                  "NamePlateId" : {
                    "description": "AmongUs NamePlate Id",
                    "type": "string",
                    "examples": [
                      "yukieiji_test_np"
                    ]
                  }
                }
              },
              "IsSameSender" : {
                "description": "Am I Sender?",
                "type": "bool",
              },
              "IsDead" : {
                "description": "Is sender dead?",
                "type": "bool",
              },
              "IsVoted" : {
                "description": "Is sender voted?",
                "type": "bool",
              }
            }
          }
        },
        "Body": {
          "description": "Chat text",
          "type": "string",
          "examples": [
            "This is chats"
          ]
        },
      }
    ]
  }
}
```

## チャットを送る
- POST : http://localhost:57700/au/chat/

| ステータスコード | 説明 |
| --- | --- |
| 200 | 追加に成功 |
| 412 | チャットを送れる状況ではない(死んでいなくて会議外やタイトル画面等) |

- パラメーター
  - `Body` string 必須
    - 追加したいチャット文字列

## 特定のサーバーのルームコードに強制的に接続させる
- POST : http://localhost:57700/au/game/

| ステータスコード | 説明 |
| --- | --- |
| 200 | 追加に成功 |
| 400 | パラメータが間違っている |
| 412 | ゲームに接続できる状態ではない(タイトル画面ではない) |

- パラメーター(**URLに埋め込んで実行する必要があります、特殊文字に関してはデコード処理を処理が入っているためエスケープ処理を行ってください**)
  - `Code` string 必須
    - ルームコード
  - `RawCode` int 必須
    - ルームコードを特定の関数を使用してint化したもの
  - `Name` string 必須
    - サーバの内部名
  - `TransName` string 必須
    - サーバの内部名を翻訳する際に使用するStringNamesを文字列化したもの

## Among Us のバニラオプションおよび役職オプションの一覧を取得

ホストのみ実行可能です。

- GET : `http://localhost:57700/au/option/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 取得に成功 |
| 400 | ロビー外など、取得できない状況 |

- レスポンス (JSON 配列)
  - 各要素:
    - `TranslatedTitle` string : カテゴリ名
    - `Options` オブジェクト配列 : オプションのリスト
      - `TranslatedTitle` string : オプション名
      - `TranslatedFormat` string : 単位などのフォーマット
      - `Value` any : 現在の値。`ValueType` が `RoleBase` の場合は以下のオブジェクト
        - `MaxCount` int : 最大出現数
        - `Chance` int : 出現確率 (%)
      - `Info` オブジェクト : オプション識別情報
        - `ValueType` string : 値の型 (`Bool`, `Byte`, `Int`, `UInt`, `Float`, `RoleBase`)
        - `OptionName` int : オプションの内部 ID
      - `Range` any[]? : 選択可能な値の範囲。`ValueType` が `RoleBase` の場合は null

### Among Us のバニラオプションを更新

ホストのみ実行可能です。

- PUT : `http://localhost:57700/au/option/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 更新に成功 |
| 400 | ホストではない、または不正なリクエスト |

- パラメーター (Body JSON)
  - `ValueType` string 必須 : 値の型 (`Bool`, `Byte`, `Int`, `UInt`, `Float`, `RoleBase`)
  - `OptionName` int 必須 : オプションの内部 ID
  - `NewValue` any 必須 : 新しい値。`RoleBase` の場合は `{"MaxCount": int, "Chance": int}` の形式。

- レスポンス (JSON)
  - `UpdatedCategory` オブジェクト? : 更新されたカテゴリの情報
    - `Id` int : カテゴリ ID
    - `Name` string : カテゴリ名
    - `ColorCode` string? : カテゴリの色 (RGBA 16進数)
    - `Options` オブジェクト配列 : オプションのリスト
      - `Id` int : オプション ID
      - `IsActive` bool : 現在有効か
      - `TranslatedName` string : 翻訳されたオプション名
      - `Selection` int : 現在の選択値（インデックス）
      - `Format` string : フォーマット
      - `RangeMeta` オブジェクト : 値の範囲に関するメタ情報
        - `Type` string : 範囲の型
        - `Values` any[] : 選択可能な値の配列
      - `Childs` オブジェクト配列 : 子オプション（階層構造がある場合）
        - `Id` int : オプション ID
        - `IsActive` bool : 有効か
        - `TranslatedName` string : 翻訳名
        - `Selection` int : 選択インデックス
        - `Format` string : フォーマット
        - `RangeMeta` オブジェクト :
          - `Type` string : 範囲の型
          - `Values` any[] : 値の配列
        - `Childs` オブジェクト配列 : さらに下位の子オプション
  - `ChainUpdatedOption` オブジェクト配列 : 連動して更新されたオプションのリスト
    - `Id` int : カテゴリ ID
    - `Options` オブジェクト配列 : オプションのリスト
      - `Id` int : オプション ID
      - `IsActive` bool : 現在有効か
      - `TranslatedName` string : 翻訳されたオプション名
      - `Selection` int : 現在の選択値（インデックス）
      - `Format` string : フォーマット
      - `RangeMeta` オブジェクト : 値の範囲に関するメタ情報
        - `Type` string : 範囲の型
        - `Values` any[] : 選択可能な値の配列
      - `Childs` オブジェクト配列 : 子オプション
        - `Id` int : オプション ID
        - `IsActive` bool : 有効か
        - `TranslatedName` string : 翻訳名
        - `Selection` int : 選択インデックス
        - `Format` string : フォーマット
        - `RangeMeta` オブジェクト :
          - `Type` string : 範囲の型
          - `Values` any[] : 値の配列
        - `Childs` オブジェクト配列 : 下位の子オプション
  - `ChainUpdateCategory` オブジェクト? : 連動して更新されたカテゴリの情報
    - `Id` int : カテゴリ ID
    - `Name` string : カテゴリ名
    - `ColorCode` string? : カテゴリの色 (RGBA 16進数)
    - `Options` オブジェクト配列 : オプションのリスト
      - `Id` int : オプション ID
      - `IsActive` bool : 現在有効か
      - `TranslatedName` string : 翻訳されたオプション名
      - `Selection` int : 現在の選択値（インデックス）
      - `Format` string : フォーマット
      - `RangeMeta` オブジェクト : 値の範囲に関するメタ情報
        - `Type` string : 範囲の型
        - `Values` any[] : 選択可能な値の配列
      - `Childs` オブジェクト配列 : 子オプション
        - `Id` int : オプション ID
        - `IsActive` bool : 有効か
        - `TranslatedName` string : 翻訳名
        - `Selection` int : 選択インデックス
        - `Format` string : フォーマット
        - `RangeMeta` オブジェクト :
          - `Type` string : 範囲の型
          - `Values` any[] : 値の配列
        - `Childs` オブジェクト配列 : 下位の子オプション

### Web設定UIを開きます
オプション設定用の Web UI (HTML) を返します。

- GET : `http://localhost:57700/au/option/ui/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 成功 |
| 404 | リソースが見つからない |


### 指定されたキーの翻訳文字列を取得

- POST : `http://localhost:57700/au/translation/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 成功 |
| 400 | 不正なリクエスト |

- パラメーター (Body JSON)
  - `Key` any 必須 : 翻訳キー（バニラの StringNames 数値、またはカスタム翻訳文字列キー）
  - `Param` any[]? : 埋め込みパラメータのリスト

- レスポンス (JSON)
  - `Key` any : リクエストされたキー（数値または文字列）
  - `Param` any[] : 翻訳に使用されたパラメータの配列
  - `Result` string : 翻訳・フォーマットされた結果の文字列

### 複数の翻訳文字列を一括取得

- POST : `http://localhost:57700/au/translation/batch/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 成功 |
| 400 | 不正なリクエスト |

- パラメーター (Body JSON 配列)
  - 各要素:
    - `Key` any 必須 : 翻訳キー
    - `Param` any[]? : 埋め込みパラメータのリスト

- レスポンス (JSON 配列)
  - 各要素:
    - `Key` any : リクエストされたキー
    - `Param` any[] : 翻訳に使用されたパラメータの配列
    - `Result` string : 翻訳・フォーマットされた結果の文字列

### オプションの単位（秒など）の翻訳一覧を一括取得

- GET : `http://localhost:57700/au/translation/batch/optionunit/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 成功 |

- レスポンス (JSON 配列)
  - 各要素:
    - `Key` any : 単位の識別子（`Second`, `Multiplier` 等の文字列）
    - `Param` any[] : パラメータ（通常は空）
    - `Result` string : 翻訳された単位文字列（例: "秒"）

### Extreme Roles で追加された全役職名の翻訳（色付き）を一括取得します。

- GET : `http://localhost:57700/au/translation/batch/role/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 成功 |

- レスポンス (JSON 配列)
  - 各要素:
    - `Key` any : 役職の内部名（`Sheriff`, `Jester` 等の文字列）
    - `Param` any[] : パラメータ（通常は空）
    - `Result` string : 翻訳・色付けされた役職名（例: "<color=#FF0000>Sheriff</color>"）

### 部屋の情報の取得

- GET : `http://localhost:57700/au/lobby/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 成功 |
| 400 | 取得に失敗（ゲームの情報が取得できない場合） |

- レスポンス (JSON)
  - `Online` オブジェクト? : オンライン情報（ローカルゲームの場合は null）
    - `MaxPlayerNum` int : 最大プレイヤー数
    - `Code` string : 部屋コード
    - `Server` string : サーバー名
  - `CurrentPlayerNames` string[] : 現在入室しているプレイヤー名のリスト