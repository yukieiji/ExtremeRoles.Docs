---
layout: default
title: 読み上げエンジン：VOICEVOX
parent: ExtremeVoiceEngine
nav_order: 1
---

- VOICEVOXによる読み上げを行うエンジン
  - [公式サイト](https://voicevox.hiroshiba.jp/)
  - 利用規約及び構成等は上記サイトをご確認ください
  - デフォルトでは「ずんだもん」の「あまあま」で読み上げを行うように設定しています
  - ここで使用しているキャラはVOICEVOXより
- このエンジンはVOICEVOXで生成した音声をAmongUsで再生しています(SEの音量指定に依存しています)

## 設定コマンド

| コマンド | 詳細 |
| --- | --- |
| /ExtremeVoiceEngine VOICEVOX<br>/eve vv | コマンドのヘルプが見れます |
| /ExtremeVoiceEngine VOICEVOX --char キャラ名 --style スタイル名 --volume ボリューム(数値) --speed スピード(数値)<br>/eve vv -c キャラ名 -s スタイル名 --volume ボリューム(数値) --speed スピード(数値) | 読み上げに使うキャラやスタイルを設定するコマンドです<br>各種値と設定値は省略可能で省略した場合は現在設定されている値を使用します<br><br>・使用例：<br>　・/eve vv -c 四国めたん -s ノーマル<br>　　・「四国めたん」の「ノーマル」で設定します（音量や話速は変更されません） |


## デフォルト設定値
- --char ずんだもん
- --style あまあま
- --volume 2.5
- --speed 1.0