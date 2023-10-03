---
layout: default
title: Extreme Skins  Creator Mode APIs
parent: REST API
nav_order: 2
---

# Extreme Skins  Creator Mode APIs

- これらのAPIはCreatorModeが有効時のみ使用可能です
  - CreatorModeの有効化方法は[こちら](https://github.com/yukieiji/ExtremeRoles/wiki/CreatorMode%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)

## Extreme Skinsの状態確認
- GET : http://localhost:57700/exs/

| ステータスコード | 説明 |
| --- | --- |
| 200 | OK |

- レスポンススキーマ
```json
{
    "type": "object",
    "properties": {
        "Status" : {
            "description": "ExS Status, Defined by https://github.com/yukieiji/ExtremeSkins.Core/blob/v2.1.1/ExtremeSkins.Core/API/StatusData.cs#L3-L7",
            "type": "string",
            "examples": [
                "Booting"
            ]
        }
        "Module" : {
            "type": "object",
            "properties": {
                "ExtremeColor": {
                    "description": "Modle:Custom Color Status, Defined by https://github.com/yukieiji/ExtremeSkins.Core/blob/v2.1.1/ExtremeSkins.Core/API/ModuleStatusData.cs#L3-L8",
                    "type": "string",
                    "examples": [
                        "Arrive"
                    ]
                },
                "ExtremeHat": {
                    "description": "Modle:Custom Hat Status, Defined by https://github.com/yukieiji/ExtremeSkins.Core/blob/v2.1.1/ExtremeSkins.Core/API/ModuleStatusData.cs#L3-L8",
                    "type": "string",
                    "examples": [
                        "Arrive"
                    ]
                },
                "ExtremeVisor": {
                    "description": "Modle:Custom Visor Status, Defined by https://github.com/yukieiji/ExtremeSkins.Core/blob/v2.1.1/ExtremeSkins.Core/API/ModuleStatusData.cs#L3-L8",
                    "type": "string",
                    "examples": [
                        "Arrive"
                    ]
                },
                "ExtremeNamePlate": {
                    "description": "Modle:Custom NamePlate Status, Defined by https://github.com/yukieiji/ExtremeSkins.Core/blob/v2.1.1/ExtremeSkins.Core/API/ModuleStatusData.cs#L3-L8",
                    "type": "string",
                    "examples": [
                        "Arrive"
                    ]
                },
            }
        }
    }
}
```

## カスタムハット一覧の取得
- GET : http://localhost:57700/exs/hat/

| ステータスコード | 説明 |
| --- | --- |
| 200 | OK |

- レスポンススキーマ
```json
[
    "type": "array",
    "Items": {
        "titele": "Hat data",
        "description": "Custom Hat Data Defined by https://github.com/yukieiji/ExtremeSkins.Core/blob/v2.1.1/ExtremeSkins.Core/API/ExportData.cs#L3",
        "type": "object",
        "properties": {
            "Id": {
                "description": "AmongUs Hat Id",
                "type": "string",
                "examples": [
                    "yukieiji_test_hat"
                ]
            },
            "Name": {
                "description": "Hat Name",
                "type": "string",
                "examples": [
                    "test_hat"
                ]
            },
            "Author": {
                "description": "Hat Author",
                "type": "string",
                "examples": [
                    "yukieiji"
                ]
            }
        }
    }
]
```

## カスタムハットの追加
- POST : http://localhost:57700/exs/hat/

| ステータスコード | 説明 |
| --- | --- |
| 200 | 追加に成功 |
| 400 | すでに同じデータが存在している等で追加に失敗 |

- パラメーター
  - `ParentPath` string 必須
    - 追加するハットのフォルダがあるパス文字列
  - `LoadFolderName` string 必須
    - 追加するハットのフォルダの名前文字列
  - `SkinName` string 必須
    - 追加するハットの名前文字列(ASCIIのみで書かれていることを推奨)
  - `AutherName` string 必須
    - 追加するハットの作者名前文字列(ASCIIのみで書かれていることを推奨)
  - `TransedSkinName` string 必須
    - 追加するハットの名前文字列(上記の`SkinName`の翻訳結果)、ない場合は空文字列を代入
  - `TransedSkinName` string 必須
    - 追加するハットの作者名前文字列(上記の`AutherName`の翻訳結果)、ない場合は空文字列を代入


## カスタムハットの更新
- PUT : http://localhost:57700/exs/hat/

| ステータスコード | 説明 |
| --- | --- |
| 200 | 更新に成功 |
| 400 | 同じハットデータが存在していない等で更新に失敗 |

- パラメーター
  - `ParentPath` string 必須
    - 更新後のハットのフォルダがあるパス文字列
  - `LoadFolderName` string 必須
    - 更新後のハットのフォルダの名前文字列
  - `SkinName` string 必須
    - 更新しようとするハットの名前文字列(ASCIIのみで書かれていることを推奨)
  - `AutherName` string 必須
    - 更新しようとするハットの作者名前文字列(ASCIIのみで書かれていることを推奨)
  - `TransedSkinName` string 必須
    - ハットの名前文字列(上記の`SkinName`の翻訳結果)、ない場合は空文字列を代入
  - `TransedSkinName` string 必須
    - ハットの作者名前文字列(上記の`AutherName`の翻訳結果)、ない場合は空文字列を代入


## カスタムバイザー一覧の取得
- GET : http://localhost:57700/exs/visor/

| ステータスコード | 説明 |
| --- | --- |
| 200 | OK |

- レスポンススキーマ
```json
[
    "type": "array",
    "Items": {
        "titele": "Visor data",
        "description": "Custom Visor Data Defined by https://github.com/yukieiji/ExtremeSkins.Core/blob/v2.1.1/ExtremeSkins.Core/API/ExportData.cs#L3",
        "type": "object",
        "properties": {
            "Id": {
                "description": "AmongUs Visor Id",
                "type": "string",
                "examples": [
                    "yukieiji_test_visor"
                ]
            },
            "Name": {
                "description": "Visor Name",
                "type": "string",
                "examples": [
                    "test_visor"
                ]
            },
            "Author": {
                "description": "Visor Author",
                "type": "string",
                "examples": [
                    "yukieiji"
                ]
            }
        }
    }
]
```

## カスタムバイザーの追加
- POST : http://localhost:57700/exs/visor/

| ステータスコード | 説明 |
| --- | --- |
| 200 | 追加に成功 |
| 400 | すでに同じデータが存在している等で追加に失敗 |

- パラメーター
  - `ParentPath` string 必須
    - 追加するバイザーのフォルダがあるパス文字列
  - `LoadFolderName` string 必須
    - 追加するバイザーのフォルダの名前文字列
  - `SkinName` string 必須
    - 追加するバイザーの名前文字列(ASCIIのみで書かれていることを推奨)
  - `AutherName` string 必須
    - 追加するバイザーの作者名前文字列(ASCIIのみで書かれていることを推奨)
  - `TransedSkinName` string 必須
    - 追加するバイザーの名前文字列(上記の`SkinName`の翻訳結果)、ない場合は空文字列を代入
  - `TransedSkinName` string 必須
    - 追加するバイザーの作者名前文字列(上記の`AutherName`の翻訳結果)、ない場合は空文字列を代入


## カスタムバイザーの更新
- PUT : http://localhost:57700/exs/visor/

| ステータスコード | 説明 |
| --- | --- |
| 200 | 更新に成功 |
| 400 | 同じバイザーデータが存在していない等で更新に失敗 |

- パラメーター
  - `ParentPath` string 必須
    - 更新後のバイザーのフォルダがあるパス文字列
  - `LoadFolderName` string 必須
    - 更新後のバイザーのフォルダの名前文字列
  - `SkinName` string 必須
    - 更新しようとするバイザーの名前文字列(ASCIIのみで書かれていることを推奨)
  - `AutherName` string 必須
    - 更新しようとするバイザーの作者名前文字列(ASCIIのみで書かれていることを推奨)
  - `TransedSkinName` string 必須
    - バイザーの名前文字列(上記の`SkinName`の翻訳結果)、ない場合は空文字列を代入
  - `TransedSkinName` string 必須
    - バイザーの作者名前文字列(上記の`AutherName`の翻訳結果)、ない場合は空文字列を代入

## カスタムネームプレート一覧の取得
- GET : http://localhost:57700/exs/nameplate/

| ステータスコード | 説明 |
| --- | --- |
| 200 | OK |

- レスポンススキーマ
```json
[
    "type": "array",
    "Items": {
        "titele": "NamePlate data",
        "description": "Custom NamePlate Data Defined by https://github.com/yukieiji/ExtremeSkins.Core/blob/v2.1.1/ExtremeSkins.Core/API/ExportData.cs#L3",
        "type": "object",
        "properties": {
            "Id": {
                "description": "AmongUs NamePlate Id",
                "type": "string",
                "examples": [
                    "yukieiji_test_nameplate"
                ]
            },
            "Name": {
                "description": "NamePlate Name",
                "type": "string",
                "examples": [
                    "test_nameplate"
                ]
            },
            "Author": {
                "description": "NamePlate Author",
                "type": "string",
                "examples": [
                    "yukieiji"
                ]
            }
        }
    }
]
```

## カスタムネームプレートの追加
- POST : http://localhost:57700/exs/visor/

| ステータスコード | 説明 |
| --- | --- |
| 200 | 追加に成功 |
| 400 | すでに同じデータが存在している等で追加に失敗 |

- パラメーター
  - `ParentPath` string 必須
    - 追加するネームプレートのフォルダがあるパス文字列
  - `LoadFolderName` string 必須
    - 追加するネームプレートのフォルダの名前文字列
  - `SkinName` string 必須
    - 追加するネームプレートの名前文字列(ASCIIのみで書かれていることを推奨)
  - `AutherName` string 必須
    - 追加するネームプレートの作者名前文字列(ASCIIのみで書かれていることを推奨)
  - `TransedSkinName` string 必須
    - 追加するネームプレートの名前文字列(上記の`SkinName`の翻訳結果)、ない場合は空文字列を代入
  - `TransedSkinName` string 必須
    - 追加するネームプレートの作者名前文字列(上記の`AutherName`の翻訳結果)、ない場合は空文字列を代入


## カスタムネームプレートの更新
- PUT : http://localhost:57700/exs/visor/

| ステータスコード | 説明 |
| --- | --- |
| 200 | 更新に成功 |
| 400 | 同じネームプレートデータが存在していない等で更新に失敗 |

- パラメーター
  - `ParentPath` string 必須
    - 更新後のネームプレートのフォルダがあるパス文字列
  - `LoadFolderName` string 必須
    - 更新後のネームプレートのフォルダの名前文字列
  - `SkinName` string 必須
    - 更新しようとするネームプレートの名前文字列(ASCIIのみで書かれていることを推奨)
  - `AutherName` string 必須
    - 更新しようとするネームプレートの作者名前文字列(ASCIIのみで書かれていることを推奨)
  - `TransedSkinName` string 必須
    - ネームプレートの名前文字列(上記の`SkinName`の翻訳結果)、ない場合は空文字列を代入
  - `TransedSkinName` string 必須
    - ネームプレートの作者名前文字列(上記の`AutherName`の翻訳結果)、ない場合は空文字列を代入