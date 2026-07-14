---
layout: default
title: ExtremeRoles API
parent: REST API
nav_order: 2
---

# ExtremeRoles API

- ExtremeRolesで追加している各種要素等にアクセスするためのAPI郡

### Extreme Rolesで追加されたカスタムオプションの一覧を取得

- GET : `http://localhost:57700/exr/option/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 取得に成功 |

- レスポンス (JSON 配列)
  - 各要素:
    - `Id` string : タブ ID
    - `Name` string : タブ名
    - `Categories` オブジェクト配列
      - `Id` int : カテゴリ ID
      - `Name` string : カテゴリ名
      - `ColorCode` string? : カテゴリの色 (RGBA 16進数)
      - `Options` オブジェクト配列
        - `Id` int : オプション ID
        - `IsActive` bool : 現在有効（表示されるべき）か
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

### Extreme Roles のカスタムオプションを更新

ホストのみ実行可能です。

- PUT : `http://localhost:57700/exr/option/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 更新に成功 |
| 202 | 更新に成功（プリセット等、全更新が必要な場合。再取得を推奨） |
| 400 | ホストではない、または不正なリクエスト |

- パラメーター (Body JSON)
  - `TabId` int 必須 : タブ ID
  - `CategoryId` int 必須 : カテゴリ ID
  - `OptionId` int 必須 : オプション ID
  - `Selection` int 必須 : 選択する値のインデックス

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

### 現在のオプション設定をエクスポート

ホストのみ実行可能です。

- GET : `http://localhost:57700/exr/option/csv/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 成功 |
| 400 | ホストではない |

- レスポンス (JSON)
  - `ExportAt` string : エクスポート日時
  - `Version` string : MOD バージョン
  - `CsvBody` string : CSV 文字列

### オプション設定をインポートして適用します

ホストのみ実行可能です。

- POST : `http://localhost:57700/exr/option/csv/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 成功 |
| 400 | 不正な CSV 形式、またはホストではない |

- パラメーター (Body JSON)
  - `CsvBody` string 必須 : インポートする CSV 文字列


### ロールアサインフィルターの取得

ホストのみ実行可能です。

- GET : `http://localhost:57700/exr/role/filter/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 成功 |

- レスポンス (JSON)
  - `FilterSet` オブジェクト : フィルタ ID (GUID) をキーとした以下のオブジェクトのマップ
    - `AssignNum` int : このフィルタに割り当てられる人数
    - `FilterNormalId` オブジェクト : このフィルタに含まれるバニラ役職の ID (int) と役職名 (string) のマップ
    - `FilterCombinationId` オブジェクト : このフィルタに含まれる組み合わせ役職の ID (int) と役職名 (string) のマップ
    - `FilterGhostRoleId` オブジェクト : このフィルタに含まれるゴースト役職の ID (int) と役職名 (string) のマップ
  - `FilterRoleId` int[] : フィルタに使用されている全役職の ID リスト
  - `NormalRoleId` オブジェクト : ID (int) からバニラ役職名 (string) へのマッピング
  - `CombinationId` オブジェクト : ID (int) から組み合わせ役職名 (string) へのマッピング
  - `GhostRoleId` オブジェクト : ID (int) からゴースト役職名 (string) へのマッピング

### ロールアサインフィルターの更新

ホストのみ実行可能です。

- POST : `http://localhost:57700/exr/role/filter/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 成功 |
| 400 | ホストではない、または不正なリクエスト |

- パラメーター (Body JSON)
  - `Op` string 必須 : 操作内容 (`FilterNewAdd`, `FilterRoleAdd`, `FilterAssignNumIncrease`, `FilterAssignNumDecrease`, `FilterRoleDelete`, `FilterDelete`)
  - `FilterId` string 必須 : フィルタ ID (GUID)
  - `MapRoleId` int? : 役職 ID（役職の追加・削除時のみ必須）


### 役職の割り当てシミュレーションを実行

ホストのみ実行可能です。

- POST : `http://localhost:57700/exr/role/simulate/`

| ステータスコード | 説明 |
| --- | --- |
| 200 | 成功 |
| 400 | リクエストの失敗（ホストではない、またはゲームが開始できる状態にない場合） |

- パラメータ (JSON)
  - `Cycle` int : 試行回数
  - `Option` オブジェクト :
    - `PlayerNum` int : プレイヤー数
  - `MockPlayerNames` string[]? : ダミープレイヤー名のリスト（任意）、未指定の場合はランダム名

- レスポンス (JSON 配列)
  - 各要素:
    - `CycleData` オブジェクト配列 : 1回ごとのアサイン結果
      - `PlayerName` string : プレイヤー名
      - `RoleName` string : 役職名
      - `Team` string : 陣営名 (`Null`, `Neutral`, `Crewmate`, `Impostor`, `Liberal`、Nullはシオンのみ使用)
