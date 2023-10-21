---
layout: default
title: CreatorMode
parent: ExtremeSkins
nav_order: 1
---

# CreatorMode

Extreme SkinsにはCreatorModeというスキン製作者向けのモードを搭載しています
## CreatorModeとは
- スキンデータのチェックと再ダウンロードを無効化することでAmongUsの起動時間を高速化します
  - これによってスキン製作者は素早くAmongUsを起動でき、スキンを素早くテストできます
- 新しい色のテストも出来るのでスキンに合った新しい色を追加することが出来ます
- 公開された新しいスキン等を反映したい場合は再度無効化すれば大丈夫です
- 有効時右上にその趣旨が表示されます

## CreatorModeの有効化方法 その1(v5.0.0.0以降可能)
1. AmongUsが起動している状態でAltキーを押しながらF12キーを押す(押すと再起動後にCreator Modeが有効になると表示されます)
2. AmongUsを再起動する

## CreatorModeの有効化方法 その2
1. AmongUs.exeのあるフォルダを開く
2. その中のBepInExフォルダ内configを開く((AmongUsのあるフォルダ/BepInEx/config))
3. me.yukieiji.extremeskins.cfgをメモ帳等で開く
4. 開いたメモ帳の中の「CreatorMode」(8行目付近)のfalseをtrueに変更する