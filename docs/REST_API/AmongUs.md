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