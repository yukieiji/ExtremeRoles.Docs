---
layout: default
title: ExtremeVoiceEngine
description: ExtremeRolesの読み上げアドオンExtreme Voice Engineについて
lang: ja_JP
nav_order: 8
has_children: true
---

# ExtremeVoiceEngine

- ExtremeRolesの状況や会議チャット等を合成音声ソフトを使うことで読み上げてくれるExtremeRoles専用のクライアント専用アドオンです
  - クライアント専用のアドオンのため全員が導入する必要はありません、必要な方だけインストールすることで動作します
  - これによって会議チャットしか出来ないようなプレイヤーが居ても状況を確認しやすくなります
    - 音声合成ソフトのインストールやライセンス認証等は必要になります
- 設定はコマンドによる操作のシンプル設計(一回設定すれば再設定の必要ありません)
- ロビーに入った時にエンジンの状況がチャットに出力されます

## コマンド

| コマンド |　詳細 |
| --- | --- |
| /ExtremeVoiceEngine<br>/eve |　コマンドのヘルプが見れます |
| /ExtremeVoiceEngine --init エンジン名<br>/ExtremeVoiceEngine -i エンジン名<br>/eve --init エンジン名<br>/eve -i エンジン名<br> | ・ ExtremeVoiceEngineで使用する音声合成ソフトを「エンジン名」で設定します<br>・エンジン名を「NONE」とすると読み上げを無効化します<br><br>・エンジン名一覧<br>　・VOICEVOX (省略系として「vv」等が使用できます) <br>　　・VOICEVOXを使った読み上げを使用します<br>　　・VOICEVOXの読み上げエンジンの設定は[こちら](https://github.com/yukieiji/ExtremeRoles/wiki/%E8%AA%AD%E3%81%BF%E4%B8%8A%E3%81%92%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%B3%EF%BC%9AVOICEVOX)を確認して下さい |

## 対応合成音声ソフト(今後も対応していきます)
- VOICEVOX
  - [公式サイト](https://voicevox.hiroshiba.jp/)
  - 利用規約及び構成等は上記サイトをご確認ください