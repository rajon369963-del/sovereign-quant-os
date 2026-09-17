# ⚡ [QUANT-SOURCE-059] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_059_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: broker-api-docs (`VAULT_IN-QUANT-003_marketcalls__broker-api-docs`)
- **Full Name**: `IN-QUANT-003_marketcalls__broker-api-docs`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Broker API Docs

A growing collection of Indian stockbroker API documentation, converted to clean Markdown for offline reading, grepping, diffing across versions, and feeding into AI coding tools (Claude Code, Cursor, GitHub Copilot, etc.) as context.

Each broker's docs live in their own folder, one Markdown file per section/page, generally sourced from the broker's official developer documentation portal.

## Brokers

| Broker | Folder | Source |
| --- | --- | --- |
| Aliceblue (ANT API v2) | [`aliceblue-api-docs/`](aliceblue-api-docs/) | https://v2api.aliceblueonline.com/ |
| AngelOne (SmartAPI) | [`angelone-api-docs/`](angelone-api-docs/) | https://smartapi.angelone.in/docs |
| Arrow Trade (REST API + Python SDK) | [`arrow-api-docs/`](arrow-api-docs/) | https://docs.arrow.trade/ |
| Definedge Securities (INTEGRATE) | [`definedge-api-docs/`](definedge-api-docs/) | https://www.definedgesecurities.com/api-documentation/ |
| Dhan (DhanHQ v2) | [`dhan-api-docs/`](dhan-api-docs/) | https://dhanhq.co/docs/v2/ |
| Flattrade (Pi) | [`flattrade-api-docs/`](flattrade-api-docs/) | https://pi.flattrade.in/docs |
| Fyers (API v3) | [`fyers-api-docs/`](fyers-api-docs/) | https://myapi.fyers.in/docsv3 |
| HDFC Sky (Open API) | [`hdfcsky-api-docs/`](hdfcsky-api-docs/) | https://developer.hdfcsky.com/sky-docs/docs/intro |
| IIFL Capital (Markets' APIs) | [`iiflcapital-api-docs/`](iiflcapital-api-docs/) | https://developers.iiflcapital.com/apidocs/introduction |
| INDstocks | [`indstocks-api-docs/`](indstocks-api-docs/) | https://api-docs.indstocks.com/ |
| Kotak Securities (Neo Trade API v2) | [`kotak-api-docs/`](kotak-api-docs/) | https://app.notion.com/p/Client-documentation-236da70d37e280b3a979fc7be7b003bc |
| Nubra | [`nubra/`](nubra/) | https://uatapi.nubra.io |
| Upstox | [`upstox-api-docs/`](upstox-api-docs/) | https://upstox.com/developer/api-documentation |
| Zerodha (Kite Connect v3) | [`zerodha-api-docs/`](zerodha-api-docs/) | https://kite.trade/docs/connect/v3/ |

More brokers will be added over time.

## Why

Broker API docs are scattered across HTML portals, PDFs, and inconsistent formats. This repo mirrors them as plain Markdown so they're easy to:

- Read and grep offline
- Diff across API versions
- Feed directly into LLM context windows for coding assistants

## Disclaimer

These are unofficial Markdown conversions maintained for personal/educational reference. Each broker's original documentation is the authoritative source — always verify against it. Trademarks and content belong to their respective brokers.

### Core Implementation Code & Architecture
#### File: `aliceblue-api-docs/postman/Aliceblue_Postman_Collection.json`
```python
{
	"info": {
		"_postman_id": "1dc7a5bd-1163-42fe-8599-b644d6476318",
		"name": "OPEN-API ALICEBLUE A3 Copy",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "39362551",
		"_collection_link": "https://kambala-7346.postman.co/workspace/ALICEBLUE~d793f93a-7d2e-4325-bc55-c18031f27ccf/collection/39362551-1dc7a5bd-1163-42fe-8599-b644d6476318?action=share&source=collection_link&creator=39362551"
	},
	"item": [
		{
			"name": "AUTH USER SESSION",
			"item": [
				{
					"name": "getUsersession",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n    \"checkSum\":\"585cd894dde1b52aec66509578ac5efd1f62d34b24cb166eb05e3de01b516787\"\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/vendor/getUserDetails",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"vendor",
								"getUserDetails"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "ORDERS",
			"item": [
				{
					"name": "place order",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "\t[\r\n    // {\r\n    //     \"exchange\": \"NSE\",\r\n    //     \"instrumentId\": \"22\",\r\n    //     \"transactionType\": \"BUY\",\r\n    //     \"quantity\": 30,\r\n    //     \"product\": \"LONGTERM\",\r\n    //     \"orderComplexity\": \"REGULAR\",\r\n    //     \"orderType\": \"LIMIT\",\r\n    //     \"validity\": \"DAY\",\r\n    //     \"price\": \"1120.15\",\r\n    //     \"slLegPrice\": \"1110.00\",\r\n    //     \"targetLegPrice\": \"3333\",\r\n    //     \"slTriggerPrice\": \"11\",\r\n    //     \"disclosedQuantity\": \"\",\r\n    //     \"marketProtectionPercent\": \"\",\r\n    //     \"deviceId\": \"123\",\r\n    //     \"trailingSlAmount\": \"\",\r\n    //     \"apiOrderSource\": \"\",\r\n    //     \"algoId\": \"\",\r\n    //      \"orderTag\":\"\"\r\n    // }\r\n    {\r\n        \"exchange\": \"NSE\",\r\n        \"instrumentId\": \"22\",\r\n        \"transactionType\": \"BUY\",\r\n        \"quantity\": 30,\r\n        \"product\": \"Intraday\",\r\n        \"orderComplexity\": \"BO\",\r\n        \"orderType\": \"SL\",\r\n        \"validity\": \"DAY\",\r\n        \"price\": \"1120.15\",\r\n        \"slLegPrice\": \"1110.00\",\r\n        \"targetLegPrice\": \"3333\",\r\n        \"slTriggerPrice\": \"11\",\r\n        \"disclosedQuantity\": \"\",\r\n        \"marketProtectionPercent\": \"\",\r\n        // \"deviceId\": \"123\",\r\n        \"trailingSlAmount\": \"\",\r\n        \"apiOrderSource\": \"\",\r\n        \"algoId\": \"\",\r\n         \"orderTag\":\"\"\r\n    }\r\n]",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/placeorder",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"placeorder"
							]
						}
					},
					"response": []
				},
				{
					"name": "modify",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n    \"brokerOrderId\": \"25071700098620\",\r\n    \"quantity\": 1,\r\n    \"orderType\": \"MARKET\",\r\n    \"slTriggerPrice\": \"8.01\",\r\n    \"price\": \"8.03\",\r\n    \"slLegPrice\": \"\", //stoploss\r\n    \"trailingSLAmount\": \"\",\r\n    \"targetLegPrice\": \"\", //targetPrice\r\n    \"validity\": \"DAY\",\r\n    \"disclosedQuantity\": \"0\",\r\n    \"marketProtection\": \"\"\r\n    // \"deviceId\": \"320de4eb90d0526d6970ee063a4b7f8e\"\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/modify",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"modify"
							]
						}
					},
					"response": []
				},
				{
					"name": "orders/checkMargin",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n    \"exchange\": \"NSE\",\r\n    \"instrumentId\": \"8479\",\r\n    \"transactionType\": \"BUY\",\r\n    \"quantity\": 1,\r\n    \"product\": \"INTRADAY\",\r\n    \"orderComplexity\": \"Regular\",\r\n    \"orderType\": \"MARKET\",\r\n    \"price\": 2830.10,\r\n    \"validity\": \" day\", \r\n    \"slLegPrice\": \"1215\",\r\n    \"slTriggerPrice\": \"0\",\r\n    \"targetLegPrice\": \"\"   \r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/checkMargin",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"checkMargin"
							]
						}
					},
					"response": []
				},
				{
					"name": "orders/history",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n            \"brokerOrderId\": \"25071400027816\"\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/history",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"history"
							]
						}
					},
					"response": []
				},
				{
					"name": "orders/cancel",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n   \"brokerOrderId\": \"25062700120949\"\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/cancel",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"cancel"
							]
						}
					},
					"response": []
				},
				{
					"name": "orders/book",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/book",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"book"
							]
						}
					},
					"response": []
				},
				{
					"name": "orders/trades",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/trades",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"trades"
							]
						}
					},
					"response": []
				},
				{
					"name": "exit bractket order",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "[{\r\n    \"brokerOrderId\":\"25051400177494\",\r\n    \"orderComplexity\":\"BO\"\r\n}]",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/exit/sno",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"exit",
								"sno"
							]
						}
					},
					"response": []
				},
				{
					"name": "Basket Margin",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "[{\r\n    \"exchange\": \"NSE\",\r\n    \"tradingSymbol\": \"TCS-EQ\",\r\n    \"price\": \"3036.8\",\r\n    \"qty\": \"1\",\r\n    \"product\": \"MTF\",\r\n    \"priceType\": \"L\",\r\n    \"triggerPrice\": \"\",\r\n    \"transType\": \"B\"\r\n}\r\n]",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/basket/margin",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"basket",
								"margin"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "GTT ORDERS",
			"item": [
				{
					"name": "Gtt Orderbook",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/gtt/orderbook",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"gtt",
								"orderbook"
							]
						}
					},
					"response": []
				},
				{
					"name": "GttOrder Cancel",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n    \"brokerOrderId\": \"25061000000166\"\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/gtt/cancel",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"gtt",
								"cancel"
							]
						}
					},
					"response": []
				},
				{
					"name": "Gtt PlaceOrder",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "// {\r\n//     \"tradingSymbol\": \"TCS-EQ\",\r\n//     \"exchange\": \"NSE\",\r\n//     \"transactionType\": \"BUY\",\r\n//     \"orderType\": \"LIMIT\",\r\n//     \"product\": \"INTRADAY\",\r\n//     \"ret\": \"DAY\",\r\n//     \"qty\": \"60\",\r\n//     \"price\": 3599,\r\n//     \"orderComplexity\": \"REGULAR\",\r\n//     \"instrumentId\": \"11536\",\r\n//     \"gttType\": \"LTP_A_O\",\r\n//     \"gttValue\": \"3599\",\r\n//     \"validity\": \"GTT\"\r\n// }\r\n\r\n{\r\n    \"tradingSymbol\": \"SILVER25SEP25C100000\",\r\n    \"exchange\": \"MCX\",\r\n    \"transactionType\": \"SELL\",\r\n    \"orderType\": \"LIMIT\",\r\n    \"product\": \"INTRADAY\",\r\n    \"validity\": \"DAY\",\r\n    \"quantity\": \"30\",\r\n    \"price\": 100,\r\n    \"orderComplexity\": \"REGULAR\",\r\n    \"instrumentId\": \"460125\",\r\n    \"gttValue\": \"12\"   \r\n}\r\n\r\n// {\r\n//     \"tradingSymbol\": \"ABCAPITAL31JUL25C300\",\r\n//     \"exchange\": \"NFO\",\r\n//     \"transactionType\": \"BUY\",\r\n//     \"orderType\": \"LIMIT\",\r\n//     \"product\": \"INTRADAY\",\r\n//     \"ret\": \"DAY\",\r\n//     \"qty\": \"10\",\r\n//     \"price\": 100,\r\n//     \"orderComplexity\": \"REGULAR\",\r\n//     \"instrumentId\": \"35098\",\r\n//     \"gttType\": \"LTP_A_O\",\r\n//     \"gttValue\": \"12\",\r\n//     \"validity\": \"GTT\"   \r\n// }",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "https://a3.aliceblueonline.com/open-api/od/v1/orders/gtt/execute",
							"protocol": "https",
							"host": [
								"a3",
								"aliceblueonline",
								"com"
							],
							"path": [
								"open-api",
								"od",
								"v1",
								"orders",
								"gtt",
								"execute"
							]
						}
					},
					"response": []
				},
				{
					"name": "Gtt Modify",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{Open_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mo
# ... [TRUNCATED FILE CONTENT]
```

#### File: `arrow-api-docs/Arrow_API.postman_collection.json`
```python
{
  "info": {
    "_postman_id": "72bc4a64-aab2-4819-93a1-5290152b17b7",
    "name": "Developer (Arrow)",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    "_exporter_id": "45071350",
    "_collection_link": "https://go.postman.co/collection/45071350-72bc4a64-aab2-4819-93a1-5290152b17b7?source=collection_link"
  },
  "item": [
    {
      "name": "Auth",
      "item": [
        {
          "name": "Authenticate Token",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n    \"checkSum\": \"ba4f6d94618ec8a56ac32e25053c20378d4cb2ad319c83bbc634ad59e160c94f\",\n    \"token\": \"01K6EWYVWWKYQXNQHEFS897S1C\",\n    \"appID\": \"90a33d77c48c\"\n}",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "https://edge.arrow.trade/auth/app/authenticate-token",
              "protocol": "https",
              "host": [
                "edge",
                "arrow",
                "trade"
              ],
              "path": [
                "auth",
                "app",
                "authenticate-token"
              ]
            }
          },
          "response": []
        }
      ]
    },
    {
      "name": "Order",
      "item": [
        {
          "name": "Place Order",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "appID",
                "value": "{{appID}}",
                "type": "text"
              },
              {
                "key": "token",
                "value": "{{token}}",
                "type": "text"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n    \"exchange\": \"NSE\",\n    \"quantity\": \"2\",\n    \"disclosedQty\": \"0\",\n    \"product\": \"I\",\n    \"symbol\": \"IDEA-EQ\",\n    \"transactionType\": \"B\",\n    \"order\": \"MKT\",\n    \"price\": \"0\",\n    \"validity\": \"DAY\",\n    \"tags\": \"strategy_1\",\n    \"amo\": false,\n    \"triggerPrice\": \"0\",\n    \"mpp\": true\n}",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "https://edge.arrow.trade/order/regular",
              "protocol": "https",
              "host": [
                "edge",
                "arrow",
                "trade"
              ],
              "path": [
                "order",
                "regular"
              ]
            }
          },
          "response": []
        },
        {
          "name": "Modify Order",
          "request": {
            "method": "PATCH",
            "header": [
              {
                "key": "appID",
                "value": "{{appID}}",
                "type": "text"
              },
              {
                "key": "token",
                "value": "{{token}}",
                "type": "text"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n    \"exchange\": \"NSE\",\n    \"quantity\": \"2\",\n    \"disclosedQty\": \"0\",\n    \"product\": \"I\",\n    \"symbol\": \"IDEA-EQ\",\n    \"transactionType\": \"B\",\n    \"order\": \"MKT\",\n    \"price\": \"0\",\n    \"validity\": \"DAY\",\n    \"tags\": \"strategy_1\",\n    \"amo\": false,\n    \"triggerPrice\": \"0\",\n    \"mpp\": true\n}",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "https://edge.arrow.trade/order/regular",
              "protocol": "https",
              "host": [
                "edge",
                "arrow",
                "trade"
              ],
              "path": [
                "order",
                "regular"
              ]
            }
          },
          "response": []
        },
        {
          "name": "Cancel Order",
          "request": {
            "method": "DELETE",
            "header": [
              {
                "key": "appID",
                "value": "{{appID}}",
                "type": "text"
              },
              {
                "key": "token",
                "value": "{{token}}",
                "type": "text"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n    \"exchange\": \"NSE\",\n    \"quantity\": \"2\",\n    \"disclosedQty\": \"0\",\n    \"product\": \"I\",\n    \"symbol\": \"IDEA-EQ\",\n    \"transactionType\": \"B\",\n    \"order\": \"MKT\",\n    \"price\": \"0\",\n    \"validity\": \"DAY\",\n    \"tags\": \"strategy_1\",\n    \"amo\": false,\n    \"triggerPrice\": \"0\",\n    \"mpp\": true\n}",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "https://edge.arrow.trade/order/regular/25120202000013",
              "protocol": "https",
              "host": [
                "edge",
                "arrow",
                "trade"
              ],
              "path": [
                "order",
                "regular",
                "25120202000013"
              ]
            }
          },
          "response": []
        },
        {
          "name": "Order Book",
          "protocolProfileBehavior": {
            "disableBodyPruning": true
          },
          "request": {
            "method": "GET",
            "header": [
              {
                "key": "appID",
                "value": "{{appID}}",
                "type": "text"
              },
              {
                "key": "token",
                "value": "{{token}}",
                "type": "text"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "https://edge.arrow.trade/user/orders",
              "protocol": "https",
              "host": [
                "edge",
                "arrow",
                "trade"
              ],
              "path": [
                "user",
                "orders"
              ]
            }
          },
          "response": []
        },
        {
          "name": "Trade Book",
          "protocolProfileBehavior": {
            "disableBodyPruning": true
          },
          "request": {
            "method": "GET",
            "header": [
              {
                "key": "appID",
                "value": "{{appID}}",
                "type": "text"
              },
              {
                "key": "token",
                "value": "{{token}}",
                "type": "text"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "https://edge.arrow.trade/user/trades",
              "protocol": "https",
              "host": [
                "edge",
                "arrow",
                "trade"
              ],
              "path": [
                "user",
                "trades"
              ]
            }
          },
          "response": []
        },
        {
          "name": "Order Details",
          "protocolProfileBehavior": {
            "disableBodyPruning": true
          },
          "request": {
            "method": "GET",
            "header": [
              {
                "key": "appID",
                "value": "{{appID}}",
                "type": "text"
              },
              {
                "key": "token",
                "value": "{{token}}",
                "type": "text"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "https://edge.arrow.trade/order/25091801000003",
              "protocol": "https",
              "host": [
                "edge",
                "arrow",
                "trade"
              ],
              "path": [
                "order",
                "25091801000003"
              ]
            }
          },
          "response": []
        }
      ]
    },
    {
      "name": "User",
      "item": [
        {
          "name": "Profile",
          "protocolProfileBehavior": {
            "disableBodyPruning": true
          },
          "request": {
            "method": "GET",
            "header": [
              {
                "key": "appID",
                "value": "{{appID}}",
                "type": "text"
              },
              {
                "key": "token",
                "value": "{{token}}",
                "type": "text"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "https://edge.arrow.trade/user/details",
              "protocol": "https",
              "host": [
                "edge",
                "arrow",
                "trade"
              ],
              "path": [
                "user",
                "details"
              ]
            }
          },
          "response": []
        }
      ]
    },
    {
      "name": "Position",
      "item": [
        {
          "name": "Positions",
          "protocolProfileBehavior": {
            "disableBodyPruning": true
          },
          "request": {
            "method": "GET",
            "header": [
              {
                "key": "appID",
                "value": "{{appID}}",
                "type": "text"
              },
              {
                "key": "token",
                "value": "{{token}}",
                "type": "text"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "https://edge.arrow.trade/user/positions",
              "protocol": "https",
              "host": [
                "edge",
                "arrow",
                "trade"
              ],
              "path": [
                "user",
                "positions"
              ]
            }
          },
          "response": []
        }
      ]
    },
    {
      "name": "Holding",
      "item": [
        {
          "name": "Holdings",
          "protocolProfileBehavior": {
            "disableBodyPruning": true
          },
          "request": {
            "method": "GET",
            "header": [
              {
                "key": "appID",
                "value": "{{appID}}",
                "type": "text"
              },
              {
                "key": "token",
                "value": "{{token}}",
                "type": "text"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "https://edge.arrow.trade/user/holdings",
              "protocol": "https",
              "host": [
                "edge",
                "arrow",
                "trade"
              ],
              "path": [
                "user",
                "holdings"
              ]
            }
          },
          "response": []
        }
      ]
    },
    {
      "name": "Utility",
      "item": [
        {
          "name": "Option Chain",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "accept",
                "value": "application/json, text/plain, */*"
              },
              {
                "key": "accept-language",
                "value": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
              },
              {
                "key": "cache-control",
                "value": "no-cache"
              },
              {
                "key": "content-type",
                "value": "application/json"
              },
              {
                "key": "dnt",
                "value": "1"
              },
              {
                "key": "origin",
                "value": "https://app.stg.arrow.trade"
              },
              {
                "key": "pragma",
                "value": "no-cache"
              },
              {
                "key": "priority",
                "value": "u=1, i"
              },
              {
                "key": "referer",
                "value": "https://app.stg.arrow.trade/"
              },
              {
                "key": "sec-ch-ua",
                "value": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\""
              },
              {
                "key": "sec-ch-ua-mobile",
                "value": "?0"
              },
              {
                "key": "sec-ch-ua-platform",
                "value": "\"macOS\""
              },
              {
                "key": "sec-fetch-dest",
                "value": "empty"
              },
              {
                "key": "sec-fetch-mode",
                "value": "cors"
              },
              {
                "key": "sec-fetch-site",
                "value": "same-site"
              },
              {
                "key": "session",
                "value": "14385063262050871829"
              },
              {
                "key": "token",
                "value": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJTSjAwMDEiLCJpc3MiOiJhcnJvdyIsInN1YiI6IndlYiIsImV4cCI6MTc2NTQ3Nzc5OSwiaWF0IjoxNzY1NDMyOTQ2fQ.Xh7jlmFxq0RfV-fhhvsvbKdqpipWgpmJsBSa_rvxu6IhywPochM0TXCdUZPu0i9sE-o3rQ8n9yIw-vyZR2UzDA"
              },
              {
                "key": "user-agent",
                "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
              },
        
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [2/3] Repository: Kotak-neo-api-v2 (`VAULT_IN-QUANT-009_Kotak-Neo__Kotak-neo-api-v2`)
- **Full Name**: `IN-QUANT-009_Kotak-Neo__Kotak-neo-api-v2`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Kotak Neo Python SDK Development

- API version: 2.0.0
- Package version: v2.0.0

## Requirements.

Python 3.10 to 3.13

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install "git+https://github.com/Kotak-Neo/Kotak-neo-api-v2.git@v2.0.2#egg=neo_api_client"
```
NOTE: For switching the version, try .git@[version number] in the above URL example .git@v1.0.0

If you are updating your package please use below command to install
```sh
pip install --force-reinstall "git+https://github.com/Kotak-Neo/Kotak-neo-api-v2.git@v2.0.2#egg=neo_api_client"
```
(you may need to run `pip` with root permission: `sudo pip install -e "`)

Then import the package:
```python
import neo_api_client
```

### Setuptools

Install via [Setuptools]

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import neo_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then refer to the sample code below for various API requests:

```python
from neo_api_client import NeoAPI


 
# access_token: It is optional. 
# environment: You pass prod to connect to live server
# neo_fin_key: It is optional. Pass None.
# consumer_key: this is the token that is available on your NEO app or website.
# To get consumer key, login to kotak NEO app or web -> invest tab -> trade api card. Generate application.
# with default application, you will have a copyable token. Pass this token in consumer_key.

client = NeoAPI(environment='prod', access_token=None, neo_fin_key=None, consumer_key='YOUR_TOKEN')


# Login using TOTP

# Complete your TOTP registration from Kotak Securities website. Follow steps mentioned below.

# Visit https://www.kotaksecurities.com/platform/kotak-neo-trade-api/ and select Register for Totp.
# Totp registration is a one time step where you can register for totp on your mobile and start receiving totps.

# Step 1 - Verify your mobile no with OTP

# Step 2 - Select account, for which you want to register for totp

# Step 3 - Select option to register for totp

# Step 4 - You will receive a QR code, which is valid for 5 minutes

# Step 5 - Open any authenticator app, and scan the QR code

# Step 6 - You will start receiving the Totps on the authenticator apps

# Step 7 - Submit the totp on the QR code page to complete the Totp registration

# mobile_number: registered mobile number with the country code.
# ucc: Unique Client Code which you will find in mobile application/website under profile section
# totp: Time-based One-Time Password recieved on google authenticator application
# totp_login generates the view token and session id used to generate trade token
client.totp_login(mobile_number="", ucc="", totp='')

# mpin: mpin for your neo account
# totp_validate generates the trade token
client.totp_validate(mpin="")



# Once you have session token after completing 2FA, you can place the order by using below function
# exchange_segment: Expected values are nse_cm, bse_cm, nse_fo, bse_fo, cde_fo, mcx_fo. 
# For exchange_segment nse_cm expected product=NRML, CNC, MIS, CO, BO. Add order_type=L, MKT, SL, SL-M. 
# For exchange_segment bse_cm expected product=NRML, CNC, MIS, CO, BO. Add order_type=L, MKT, SL, SL-M.
# For exchange_segment nse_fo expected product=NRML, MIS, BO. Add order_type=L, MKT, SL, SL-M.
# For exchange_segment bse_fo expected product=NRML, MIS. Add order_type=L, MKT, SL, SL-M.
# For exchange_segment mcx_fo expected product=NRML, MIS. Add order_type=L, MKT, SL, SL-M.

# For exchange_segment cde_fo expected product=NRML, MIS. Add order_type=L, MKT, SL, SL-M.

# product: Expected values are NRML, CNC, MIS, CO, BO, MTF
# price: scrip price
# order_type: Expected values are L, MKT, SL, SL-M
# quantity: The stock quantity(If suppose one lot size of a stock is 25, then in disclosed_quantity you have to pass 25 and not 1)
# validity: Expected values are DAY, IOC, GTC, EOS, GTD
# trading_symbol: scrip trading symbol. You will get this value from master scrip file
# transaction_type: Expected values are B, S
# amo: Expected values are either YES or NO
# disclosed_quantity: by default 0. Disclosed quantity (DQ) is a feature that allows traders to only disclose a portion of their order quantity to the market. This feature is useful when trading large quantities of shares. For example, if your quantity is 10, then disclosed_quantity can be between 0 to 10 (only disclosed _quantity will be visible in market depth)
# market_protection: by default 0. Market protection, also known as Market Price Protection (MPP), is a feature that protects investors from sudden price movements in the stock market. For example, if the Last Traded Price (LTP) is ₹100 and a 5% Market Protection is applied, your order will be placed as a limit order at ₹105. This means your buy order will only be executed if sellers are available at ₹105 or below. If no sellers are available within this range, your order will remain open as a limit order.
# pf: by default N
# trigger_price: Price on which ypur order will be open to the market
# tag: Give your own tag to track the order
# scrip_token: Applicable only for Bracket Order
# square_off_type: Applicable only for Bracket Order. Expected Values are 'Absolute' and 'Ticks'.
# stop_loss_type: Applicable only for bracket Order. Expected Values are 'Absolute' and 'Ticks'.
# stop_loss_value: Applicable only for Bracket Order
# square_off_value: Applicable only for Bracket Order
# last_traded_price: Applicable only for Bracket Order
# trailing_stop_loss: Applicable only for Bracket Order. Expected Values are 'Y' and 'N'.
# trailing_sl_value: Applicable only for Bracket Order. Expected Values are 'Y' and 'N'.	
client.place_order(
    exchange_segment="",
    product="",
    price="",
    order_type="",
    quantity="",
    validity="",
    trading_symbol="",
    transaction_type="",
    amo="NO",
    disclosed_quantity="0",
    market_protection="0",
    pf="N",
    trigger_price="0",
    tag=None,
    scrip_token=None,
    square_off_type=None,
    stop_loss_type=None,
    stop_loss_value=None,
    square_off_value=None,
    last_traded_price=None,
    trailing_stop_loss=None,
    trailing_sl_value=None,
)


						
# Modify an order
# order_id: Order number you'll recieve from the response after placing the order
# price: scrip price
# quantity: The stock quantity(If suppose one lot size of a stock is 25, then in disclosed_quantity you have to pass 25 and not 1)
# disclosed_quantity: by default 0. Disclosed quantity (DQ) is a feature that allows traders to only disclose a portion of their order quantity to the market. This feature is useful when trading large quantities of shares. For example, if your quantity is 10, then disclosed_quantity can be between 0 to 10 (only disclosed _quantity will be visible in market depth)
# trigger_price: Price on which ypur order will be open to the market
# validity: Expected values are DAY, IOC, GTC, EOS, GTD
# order_type: Expected values are L, MKT, SL, SL-M
client.modify_order(order_id = "", price = "7.0", quantity = "2", disclosed_quantity = "0", trigger_price = "0", validity = "DAY", order_type='')

# Cancel an order
# order_id: Order number you'll recieve from the response after placing the order
client.cancel_order(order_id = "")

# order_id: Order number you'll recieve from the response after placing the order
# isVerify: isVerify is an optional param. Default value is 'False'. If isVerify is True, we will first check the status of the given order. If the order status is not 'rejected', 'cancelled', 'traded', or 'completed', we will proceed to cancel the order using the cancel_order function. Otherwise, we will display the order status to the user instead.
# amo: It specifies whether its an after market order. Expected values are YES and NO
# This request will check whether your order is rejected, cancelled, complete or traded. If any of this is true, your order will not be cancelled. This will be rejected with the rejection reson. 
# If this is not the case, the your order will be cancelled.
client.cancel_order(order_id = "", amo = "", isVerify=True)


# Cancel cover order
# order_id: Order number you'll recieve from the response after placing the order
client.cancel_cover_order(order_id = "")
# order_id: Order number you'll recieve from the response after placing the order
# isVerify: isVerify is an optional param. Default value is 'False'. If isVerify is True, we will first check the status of the given order. If the order status is not 'rejected', 'cancelled', 'traded', or 'completed', we will proceed to cancel the order using the cancel_order function. Otherwise, we will display the order status to the user instead.
# This request will check whether your order is rejected, cancelled, complete or traded. If any of this is true, your order will not be cancelled. This will be rejected with the rejection reson. 
# amo: It specifies whether its an after market order. Expected values are YES and NO
client.cancel_cover_order(order_id = "", amo = "", isVerify=False)

# Cancel bracket order
# Cancel cover order
# order_id: Order number you'll recieve from the response after placing the order
client.cancel_bracket_order(order_id = "")
# order_id: Order number you'll recieve from the response after placing the order
# isVerify: isVerify is an optional param. Default value is 'False'. If isVerify is True, we will first check the status of the given order. If the order status is not 'rejected', 'cancelled', 'traded', or 'completed', we will proceed to cancel the order using the cancel_order function. Otherwise, we will display the order status to the user instead.
# This request will check whether your order is rejected, cancelled, complete or traded. If any of this is true, your order will not be cancelled. This will be rejected with the rejection reson. 
# amo: It specifies whether its an after market order. Expected values are YES and NO
client.cancel_bracket_order(order_id = "", amo = "", isVerify=False)


# Get Order Book
# The function retrieves a list of orders in the order book.
client.order_report()

# Get Order History
# The function retrieves the order history for a given order ID.
# order_id: Order number you'll recieve from the response after placing the order
client.order_history(order_id = "")

# Get Trade Book
# The function retrieves a filtered list of trades.
client.trade_report()

# Get Detailed Trade Report for specific order id. 
# The function retrieves a filtered list of trades.
# order_id: Order number you'll recieve from the response after placing the order
client.trade_report(order_id = "")

# Get Positions
# The function retrieves a list of positions
client.positions()

# Get Portfolio Holdings
# The function retrieves the current holdings for the portfolio
client.holdings()

# Get Limits
# The function retrieves the limits available for the given segment, exchange and product
# segment: Expected values are CASH, CUR, FO, ALL. Default value is 'ALL'
# exchange: Expected values are ALL, NSE, BSE
# product: Expected values are NRML, CNC, MIS, ALL
client.limits(segment="", exchange="", product="")

# Get Margin required for Equity orders. 
# The function calculates the margin required for a given trade.
# exchange_segment: Expected values are nse_cm, bse_cm, nse_fo, bse_fo, cde_fo, mcx_fo. 
# price: scrip price
# order_type: Expected values are L, MKT, SL, SL-M
# product: Expected values are NRML, CNC, MIS, CO, BO
# quantity: The stock quantity
# instrument_token: The instrument token of the stock to trade.
# transaction_type: Expected values are B, S
client.margin_required(exchange_segment = "", price = "", order_type= "", product = "",   quantity = "", instrument_token = "",  transaction_type = "")

# Get Scrip Master CSV file
# The function retrieves the list of scrips available in the given exchange segment
client.scrip_master()

# Get Scrip Master CSV file for specific Exchange Segment. 
# exchange_segment: Section of a stock exchange. Its a mandatory param. Expected values are nse_cm, bse_cm, nse_fo, bse_fo, cde_fo, mcx_fo
client.scrip_master(exchange_segment = "")

# Search for the Scrip details from Scrip master file
# exchange_segment: Section of a stock exchange. Its a mandatory param. Expected values are nse_cm, bse_cm, nse_fo, bse_fo, cde_fo, mcx_fo
client.search_scrip(exchange_segment="", symbol="", expiry="", option_type="",
                    strike_price="")

# Get quote details
instrument_tokens = [
    {"instrument_token": "", "exchange_segment": ""},
    {"instrument_token": "", "exchange_segment": ""},
    {"instrument_token": "", "exchange_segment": ""}
]
# quote_type: Expected values are `all`, `depth`, `ohlc`, `ltp`, `oi`, `52w`, `circuit_limits`, `scrip_details`
    # By default, `quote_type` is set as `all`, which means you will get the complete data.
    # Quotes API can be accessed by access token without completing login.
# instrument_tokens: This is a list of dictionaries.
    # instrument_token: The instrument token of the stock
    # exchange_segment: Expected values are nse_cm, bse_cm, nse_fo, bse_fo, cde_fo, mcx_fo
client.quotes(instrument_tokens = instrument_tokens, quote_type = "")

def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)

def on_close(message):
    print(message)
    
def on_open(message):
    print(message)

# Setup Callbacks for websocket events (Optional)
client.on_message = on_message  # called when message is received from websocket
client.on_error = on_error  # called when any error or exception occurs in code or websocket
client.on_close = on_close  # called when websocket connection is closed
client.on_open = on_open  # called when websocket successfully connects

# Subscribe method will get you the live feed details of the given tokens.
# By Default isIndex is set as False and you want to get the live feed to index scrips set the isIndex flag as True 
# By Default isDepth is set as False and you want to get the depth information set the isDepth flag as True
# instrument_tokens: This is a list of dictionaries.
    # instrument_token: The instrument token of the stock which you will get from master scrip file
    # exchange_segment: Expected values are nse_cm, bse_cm, nse_fo, bse_fo, cde_fo, mcx_fo
# isIndex: If you want to subscribe to index data, set isIndex to True
# isDepth: If you want to subscribe to depth data, set isDepth to True
client.subscribe(instrument_tokens = instrument_tokens, isIndex=False, isDepth=False)

# Un_Subscribes the given tokens. First the tokens will be checked weather that is subscribed. If not Subscribed we will send you the error message else we will unsubscribe the give tokens
# instrument_tokens: This is a list of dictionaries.
    # instrument_token: The instrument token of the stock
    # exchange_segment: Expected values are nse_cm, bse_cm, nse_fo, bse_fo, cde_fo, mcx_fo
# isIndex: If you want to unsubscribe to index data, set isIndex to True
# isDepth: If you want to unsubscribe to depth data, set isDepth to True
client.un_subscribe(instrument_tokens=instrument_tokens, isIndex=False, isDepth=False)

#Order Feed 
# This function subscribes to order feed
client.subscribe_to_orderfeed()

#Terminate user's Session
client.logout()
```


## Documentation for API Endpoints

| Class                  | Method                                                                                     | Description              |
|------------------------|--------------------------------------------------------------------------------------------|--------------------------|
| *Session Initiation*   | [**neo_api_client.SessionINIT**](docs/Session_init.md#session_init)                        | Initialise Session       |
| *TOTP LoginAPI*        | [**neo_api_client.Totp_login**](docs/Totp_login.md#totp_login)                             | TOTP Login               |
| *TOTP LoginAPI*        | [**neo_api_client.Totp_validation**](docs/Totp_validate.md#totp_validate)                  | TOTP Validation          |
| *Place Order*          | [**neo_api_client.placeorder**](docs/Place_Order.md#place_order)                           | Place Order              |
| *Modify Order*         | [**neo_api_client.modifyorder**](docs/Modify_Order.md#modify_order)                        | Modify Order             |
| *Cancel Order*         | [**neo_api_client.cancelorder**](docs/Cancel_Order.md#cancel_order)                        | Cancel Order             |
| *Cancel Order*         | [**neo_api_client.cancelcoverorder**](docs/Cancel_Cover_Order.md#cancel_cover_order)       | Cancel Cover Order       |
| *Cancel Order*         | [**neo_api_client.cancelbracketorder**](docs/Cancel_Bracket_Order.md#cancel_bracket_order) | Cancel Bracket Order     |
| *Order Report*         | [**neo_api_client.orderreport**](docs/Order_report.md#order_report)                        | Order Report             |
| *Order History*        | [**neo_api_client.orderhistory**](docs/Order_history.md#order_history)                     | Order Report             |
| *Trade Report*         | [**neo_api_client.tradereport**](docs/Trade_report.md#trade_report)                        | Trade Report             |
| *Positions*            | [**neo_api_client.positions**](docs/Positions.md#positions)                                | Positions                |
| *Holdings*             | [**neo_api_client.holdings**](docs/Holdings.md#holdings)                                   | Holdings                 |
| *Limits*               | [**neo_api_client.limits**](docs/Limits.md#limits)                                         | Limits                   |
| *Margin Required*      | [**neo_api_client.margin_required**](docs/Margin_Required.md#margin_required)              | Margin Required          |
| *Scrip Master*         | [**neo_api_client.scrip_master**](docs/Scrip_Master.md#scrip_master)                       | Scrip Master             |
| *Search Scrip*         | [**neo_api_client.scrip_search**](docs/Scrip_Search.md#scrip_search)                       | Scrip Search             |
| *Quotes*               | [**neo_api_client.quotes**](docs/Quotes.md#quotes)                                         | Quotes                   |
| *Subscribe*            | [**neo_api_client.subscribe**](docs/webSocket.md#websocket)                                | Subscribe                |
| *Subscribe Order Feed* | [**neo_api_client.subscribeorderfeed**](docs/webSocket_orderfeed.md#websocket_orderfeed)   | Subscribe                |

### Core Implementation Code & Architecture
#### File: `setup.py`
```python
from setuptools import setup, find_packages

NAME = "neo-api-client"
VERSION = "2.0.0"
# To install the library, run the following
#
# python setup.py install

REQUIRES = ['bidict==0.22.1', 'certifi==2022.12.7', 'idna==2.10', 'numpy==2.1.0', 'pyjsparser==2.7.1', 'PyJWT==2.6.0',
            'python-dateutil==2.8.2', 'python-dotenv==1.0.0', 'requests==2.32.3', 'six==1.16.0', 'urllib3==1.26.14',
            'websocket-client==1.8.0', 'websockets==8.1', 'pandas==2.2.3', 'asyncio==3.4.3']

setup(
    name=NAME,
    version=VERSION,
    description="Neo Trade API",
    author="ne API",
    author_email="",
    url="",
    keywords=["Neo-Trade API", "Neo Trade API's"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    """
)
```

#### File: `neo_api_client/api/__init__.py`
```python
from __future__ import absolute_import

from neo_api_client.api.login_api import LoginAPI
from neo_api_client.api.order_api import OrderAPI
from neo_api_client.api.order_report_api import OrderReportAPI
from neo_api_client.api.order_history_api import OrderHistoryAPI
from neo_api_client.api.trade_report_api import TradeReportAPI
from neo_api_client.api.modify_order_api import ModifyOrder
from neo_api_client.api.modify_order_api import ModifyOrder
from neo_api_client.api.positions_api import PositionsAPI
from neo_api_client.api.portfolio_holdings_api import PortfolioAPI
from neo_api_client.api.margin_api import MarginAPI
from neo_api_client.api.scrip_master_api import ScripMasterAPI
from neo_api_client.api.limits_api import LimitsAPI
from neo_api_client.api.logout_api import LogoutAPI
from neo_api_client.api.totp_api import TotpAPI
```

#### File: `neo_api_client/api/logout_api.py`
```python
from neo_api_client.exceptions import ApiException


class LogoutAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = api_client.rest_client

    def logging_out(self):
        header_params = {
            "Authorization": "Bearer " + self.api_client.configuration.bearer_token,
            "Sid": self.api_client.configuration.edit_sid,
            "Auth": self.api_client.configuration.edit_token,
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        URL = self.api_client.configuration.get_url_details("logout")

        try:
            logout_report = self.rest_client.request(
                url=URL, method='POST',
                headers=header_params
            )
            return {"data": logout_report.text}
        except ApiException as ex:
            return {"error": ex}
```

#### File: `neo_api_client/api/portfolio_holdings_api.py`
```python
import requests


class PortfolioAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = api_client.rest_client

    def portfolio_holdings(self):
        header_params = {
            "Sid": self.api_client.configuration.edit_sid,
            "Auth": self.api_client.configuration.edit_token,
            'accept': '*/*'
        }
        params = {"sId": self.api_client.configuration.serverId}

        URL = self.api_client.configuration.get_url_details("holdings")
        try:
            portfolio_report = self.rest_client.request(
                url=URL, method='GET',
                query_params=None,
                headers=header_params
            )
            return portfolio_report.json()
        except requests.exceptions.RequestException as e:
            # handle any exceptions that might be raised here
            print(f"Error occurred: {e}")
```

#### File: `neo_api_client/api/order_report_api.py`
```python
import requests


class OrderReportAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = api_client.rest_client

    def ordered_books(self):
        header_params = {
            "Sid": self.api_client.configuration.edit_sid,
            "Auth": self.api_client.configuration.edit_token,
            "accept": "application/json"
        }
        query_params = {"sId": self.api_client.configuration.serverId}

        URL = self.api_client.configuration.get_url_details("order_book")

        try:
            order_report = self.rest_client.request(
                url=URL, method='GET',
                query_params=query_params,
                headers=header_params
            )
            return order_report.json()
        except requests.exceptions.RequestException as e:
            # handle any exceptions that might be raised here
            print(f"Error occurred: {e}")
```

#### File: `neo_api_client/api/positions_api.py`
```python
import requests


class PositionsAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = api_client.rest_client

    def position_init(self):
        header_params = {
            "Sid": self.api_client.configuration.edit_sid,
            "Auth": self.api_client.configuration.edit_token,
            "accept": "application/json"
        }
        query_params = {"sId": self.api_client.configuration.serverId}

        URL = self.api_client.configuration.get_url_details("positions")
        try:
            position_report = self.rest_client.request(
                url=URL, method='GET',
                query_params=query_params,
                headers=header_params
            )
            return position_report.json()
        except requests.exceptions.RequestException as e:
            # handle any exceptions that might be raised here
            print(f"Error occurred: {e}")
```


==================================================


## [3/3] Repository: kotak-neo-python (`VAULT_IN-QUANT-011_Kotak-Neo__kotak-neo-python`)
- **Full Name**: `IN-QUANT-011_Kotak-Neo__kotak-neo-python`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Kotak Neo API - Python SDK

Official Python SDK for Kotak Neo Trading APIs - a modern, well-tested trading client for the Kotak Neo platform.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![PyPI Version](https://img.shields.io/badge/pypi-v3.0.7-green.svg)](https://pypi.org/project/kotakneoapi/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/LICENSE)

> **This is the actively maintained Python SDK**, superseding
> [`kotak-neo-api-v2`](https://github.com/Kotak-Neo/kotak-neo-api-v2) (now legacy).
> Already on `kotak-neo-api-v2`? See the
> **[Migration Guide](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/guides/MIGRATION.md)**.

## Features

✅ **Authentication** - TOTP-based secure login with 2FA  
✅ **Order Management** - Place, modify, cancel orders (Regular/AMO)  
✅ **Portfolio & Positions** - Real-time holdings, positions, and limits  
✅ **Market Data** - Live quotes, scrip master, search functionality, expiries, option chain, and historical candle data  
✅ **SFeed WebSocket Streaming** - Modern async/await live market feed with typed messages, enriched with `trading_symbol`  
✅ **HTTP/2 Transport** - REST calls use HTTP/2 (via httpx) with automatic HTTP/1.1 fallback  
✅ **Optional Reliability Utilities** - Opt-in rate limiting, plus retry and circuit-breaker helpers  
✅ **Enhanced Logging** - Rotating log file with REST/WebSocket tracking and automatic masking of sensitive data  
✅ **Comprehensive Error Handling** - Detailed exception hierarchy with input validation  
✅ **Type Safety** - Full mypy type checking support  
✅ **Extensive Testing** - 100% test coverage (unit, integration, and E2E tests)  

## Installation

### From PyPI

```bash
pip install kotakneoapi
```

### For Development (Local Installation)

```bash
# Clone the repository
git clone https://github.com/Kotak-Neo/kotak-neo-python.git
cd kotak-neo-python

# Install in development/editable mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

## Quick Start

### Prerequisites

1. **Get Consumer Key (REQUIRED)**: Login to Kotak NEO app/web → **More** tab → **Trade API** card → Generate application → Copy the token
   - This token is used in the Authorization header for all API requests
   - Authentication will fail without this token
2. **Register for TOTP**: Visit API Dashboard (Neo App/Web → more tab → trade API), on top right menu bar click "TOTP Registration" → Register for TOTP → Scan QR code with authenticator app (Google Authenticator, Authy, etc.)

### Getting started with quick order placement

```python
from neo_api_client import NeoAPI

# Initialize the client
client = NeoAPI(
    consumer_key="your-consumer-key-token",  # Token from NEO app Trade API card
    environment="prod",  # production (default)
    access_token=None,  # Optional
    neo_fin_key=None,  # Optional
)

# Step 1: Login with TOTP
login_response = client.totp_login(
    mobile_number="+919876543210",  # Your registered mobile with country code
    ucc="YOUR_UCC",  # Find in NEO app/web under Profile section
    totp="123456",  # 6-digit code from authenticator app (changes every 30 seconds)
)

# Step 2: Validate with MPIN to complete authentication
validate_response = client.totp_validate(mpin="123456")  # Your trading MPIN

# Place an order
order_response = client.place_order(
    exchange_segment="nse_cm",
    product="CNC",
    price="1500.00",
    order_type="L",
    quantity="10",
    validity="DAY",
    trading_symbol="RELIANCE-EQ",
    transaction_type="B",
)

# Get real-time quotes
quotes = client.quotes(
    instrument_tokens=[{"instrument_token": "1333", "exchange_segment": "nse_cm"}], quote_type="all"
)

# Logout
client.logout()
```

## Documentation

### 📚 [Complete API Documentation](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/README.md)

Detailed documentation for all SDK functions with examples and real API responses.

#### Quick Links

**Authentication**
- [TOTP Login](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/authentication/totp_login.md) | [TOTP Validate](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/authentication/totp_validate.md) | [What's My IP](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/authentication/whatsmyip.md) | [Logout](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/authentication/logout.md)

**Order Management**
- [Place Order](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/orders/place_order.md) | [Modify Order](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/orders/modify_order.md) | [Cancel Order](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/orders/cancel_order.md)
- [Order Report](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/orders/order_report.md) | [Order History](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/orders/order_history.md) | [Trade Report](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/orders/trade_report.md)

**Portfolio & Positions**
- [Holdings](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/portfolio/holdings.md) | [Positions](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/portfolio/positions.md)
- [Limits](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/portfolio/limits.md) | [Margin Required](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/portfolio/margin_required.md)

**Market Data**
- [Quotes](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/market_data/quotes.md) | [Scrip Master](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/market_data/scrip_master.md) | [Search Scrip](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/market_data/search_scrip.md)
- [Expiries](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/market_data/expiries.md) | [Option Chain](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/market_data/option_chain.md) | [Historical Data](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/market_data/historical_data.md)

**WebSocket**
- Market data (SFeed): [Market Feed (Subscribe/Unsubscribe)](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/websocket/market_feed.md)
- Order & positions: [Order Feed](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/websocket/order_feed.md)
- Full guide: [SFeed WebSocket](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/guides/websocket.md)

### 📖 Guides & Documentation

**Upgrading:**
- **[Migration Guide (v2.0.2 → v3.0.X)](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/guides/MIGRATION.md)** - Upgrade existing code to the latest version
- **[Migration Scanner](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/scripts/migrate_from_v2.py)** - Run against your project to auto-detect v2-only calls before you start migrating by hand

**Installation:**
- **[Installation Overview](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/installation/README.md)** - All installation options
- **[Local Installation](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/installation/local-install.md)** - Install from source (for contributors)
- **[Platform-Specific Guides](https://github.com/Kotak-Neo/kotak-neo-python/tree/main/docs/installation)** - Windows, macOS, Linux, VS Code
- **[Jupyter Notebook Setup](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/installation/jupyter.md)** - Kernel setup and using `await` directly in cells (no `asyncio.run()`)

**API Documentation:**
- **[Complete API Reference](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/README.md)** - All SDK functions
- **[SFeed WebSocket Guide](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/guides/websocket.md)** - Async streaming client, protocol & migration
- **[Sync/Multi-Process Integration Guide](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/guides/sync-integration.md)** - Bridging the async feeds into gunicorn/Celery-style sync, multi-process apps
- **[Logging Guide](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/guides/logging.md)** - `setup_logging()`, log levels & configuration
- **[All Guides](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/guides/README.md)** - Complete guide index

## WebSocket Streaming Example (SFeed)

Live market data is delivered through the modern async/await **SFeed** WebSocket
client. It uses `async for` iteration and returns type-safe Pydantic messages,
each enriched with its `trading_symbol` (resolved from the subscribe ack) —
except `SFeedMarketStatus`, which isn't tied to a specific instrument (see
below).

```python
import asyncio
from neo_api_client import NeoAPI
from neo_api_client.websocket.feed import WsToken, SFeedScrip, SFeedMarketStatus


async def main():
    client = NeoAPI(consumer_key="your-consumer-key-token", environment="prod")
    client.totp_login(mobile_number="+919876543210", ucc="YOUR_UCC", totp="123456")
    client.totp_validate(mpin="123456")

    # create_websocket() builds a SFeedWebSocket from the current session
    async with client.create_websocket() as ws:
        # Batch-subscribe any number of instruments in a single call
        await ws.subscribe_scrips([
            WsToken("nse_cm", "Nifty 50"),
            WsToken("nse_cm", "11536"),
        ])

        async for message in ws:
            if isinstance(message, SFeedScrip):
                print(
                    f"{message.trading_symbol} ({message.instrument_token}) "
                    f"LTP: {message.last_traded_price}"
                )


asyncio.run(main())
```

Market status (open/close/pre-open/etc., not tied to a specific instrument) is a
separate subscription — `subscribe_exchange()` takes no tokens and delivers
`SFeedMarketStatus`:

```python
await ws.subscribe_exchange()

async for message in ws:
    if isinstance(message, SFeedMarketStatus):
        print(f"status_code={message.status_code} status={message.status}")
```

`status` is a static, human-readable string (e.g. `"Market open"`) looked up by
`status_code` — not the raw wire text, which is unreliable in practice. See
[Message Types](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/guides/websocket.md#message-types)
in the guide for the full `MarketStatusCode` table.

> **Note:** The SFeed client works out of the box — its dependencies
> (`websockets`, `pydantic`) ship with the base install. The legacy callback-based
> WebSocket (`client.subscribe(...)`, `on_message`, etc.) was **removed in v2.2.0** —
> see the [SFeed WebSocket guide](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/guides/websocket.md) for the full API and a
> migration reference.

> **Running this in Jupyter Notebook instead of a script?** Don't wrap it in
> `asyncio.run()` — Jupyter's kernel already runs its own event loop, so
> `await` the client's coroutines directly in a cell instead. See the
> [Jupyter Notebook Setup guide](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/installation/jupyter.md) for the notebook-adapted version of this example and Jupyter-specific troubleshooting.

## Order & Position Streaming Example

Order-lifecycle events and live position updates stream over a separate
async/await WebSocket, `create_order_feed()`. It returns type-safe `OrderUpdate` /
`PositionUpdate` messages.

```python
import asyncio
from neo_api_client import NeoAPI
from neo_api_client.websocket.orderfeed import OrderUpdate, PositionUpdate, OrderStatus


async def main():
    client = NeoAPI(consumer_key="your-consumer-key-token", environment="prod")
    client.totp_login(mobile_number="+919876543210", ucc="YOUR_UCC", totp="123456")
    client.totp_validate(mpin="123456")

    # create_order_feed() connects to wss://<baseurl>/realtime using the session
    async with client.create_order_feed() as feed:
        async for message in feed:
            if isinstance(message, OrderUpdate):
                print(f"order {message.data.order_no} -> {message.data.order_status}")
            elif isinstance(message, PositionUpdate):
                print(f"position {message.data.symbol}")


asyncio.run(main())
```

> Full reference: [Order & Position Feed](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/functions/websocket/order_feed.md).

## Exception Handling

```python
from neo_api_client import (
    NeoAPIException,
    AuthenticationError,
    ValidationError,
    RateLimitError,
    NetworkError,
    OrderError,
)

try:
    response = client.place_order(...)
except AuthenticationError:
    print("Authentication failed - please login again")
except ValidationError as e:
    print(f"Invalid parameters: {e}")
except RateLimitError:
    print("Rate limit exceeded - please retry after some time")
except OrderError as e:
    print(f"Order placement failed: {e}")
except NeoAPIException as e:
    print(f"API error: {e}")
```

## Environment Setup

Create a `.env` file for credentials (copy from `.env.example`):

```bash
# Consumer Key from NEO app (REQUIRED - Used in Authorization header)
# Get it: NEO app → More → Trade API → Generate application → Copy token
NEO_CONSUMER_KEY=your-consumer-key-token

# Your registered mobile number with country code
NEO_MOBILE_NUMBER=+919876543210

# Your UCC (User Client Code) from NEO app Profile section
NEO_UCC=YOUR_UCC

# Your trading MPIN
NEO_MPIN=123456
```

**How to get credentials:**
- **Consumer Key**: NEO app → More → Trade API → Generate application → Copy token
- **UCC**: NEO app → Profile section

> TOTP is a 2FA factor and is intentionally not automated via a `.env` secret here — `totp_login()` expects the live 6-digit code. See [`tests/e2e/smoke_test.py`](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/tests/e2e/smoke_test.py) for an example that prompts for it (or optionally auto-generates it from a `NEO_TOTP_SECRET` you add to your own local `.env`, for faster local iteration only).



## Common Parameters

### Exchange Segments
- `nse_cm` - NSE Cash Market
- `bse_cm` - BSE Cash Market
- `nse_fo` - NSE Futures & Options
- `bse_fo` - BSE Futures & Options
- `mcx_fo` - MCX Commodities
- `cde_fo` - Currency Derivatives (market data/quotes only — **not** accepted by `place_order`/`margin_required`, which don't support this segment)

### Product Types
- `CNC` - Cash & Carry (Delivery)
- `MIS` - Margin Intraday Square-off
- `NRML` - Normal (Carry Forward)
- `MTF` - Margin Trading Facility

Note: `place_order`/`modify_order` only accept these four exact codes (Bracket
and Cover orders are no longer supported).

### Order Types
- `L` - Limit Order
- `MKT` - Market Order
- `SL` - Stop Loss Limit
- `SL-M` - Stop Loss Market

### Transaction Types
- `B` - Buy
- `S` - Sell

### Validity Types
- `DAY` - Valid for the day
- `IOC` - Immediate or Cancel

## Architecture

Always on for every request:

- **HTTP/2 Transport** - REST calls run over HTTP/2 (via `httpx`) with connection pooling and automatic HTTP/1.1 fallback
- **Structured Logging** - Request/response tracking with correlation IDs
- **Type Safety** - Full mypy type checking support

Optional reliability utilities (shipped, tested, and importable, but **not wired
into the request path by default** — you opt in):

- **Rate Limiter** - Token-bucket throttling (per second/minute/hour) to avoid tripping API quotas. Enable with `RESTClientObject(..., enable_rate_limiting=True)`.
- **Retry Logic** - Exponential backoff with jitter for transient errors, via the `with_retry` / `create_retry_decorator` decorators in `neo_api_client.retry`.
- **Circuit Breaker** - `CircuitBreaker` in `neo_api_client.circuit_breaker` to stop calling a failing service and let it recover.

### Custom Transport (Migration Hook)

Deployments that previously patched the legacy `requests`-based client's
connection pool/adapter (custom proxy, mTLS, non-default pool sizing,
transport-level instrumentation) have the equivalent hook here via `httpx`'s
own extension points, passed straight through to `NeoAPI(...)`:

```python
import httpx
from neo_api_client import NeoAPI

# Full control: mount a custom transport (proxy, mTLS, custom pooling, etc.)
client = NeoAPI(
    consumer_key="your-consumer-key-token",
    transport=httpx.HTTPTransport(
        proxy="https://proxy.internal:8080", cert=("client.pem", "client.key")
    ),
)

# Or just resize the connection pool without a full custom transport:
client = NeoAPI(
    consumer_key="your-consumer-key-token",
    limits=httpx.Limits(max_connections=50, max_keepalive_connections=20),
)
```

`limits` is ignored when `transport` is also given, since a custom transport
owns its own pooling. Both default to the SDK's existing behavior
(`max_connections=20`, `max_keepalive_connections=10`, standard `httpx`
transport) when omitted.

**HTTP/2 and timeouts** are also configurable per client:

```python
client = NeoAPI(
    consumer_key="your-consumer-key-token",
    http2=False,  # force HTTP/1.1 only; default is True (HTTP/2 with automatic HTTP/1.1 fallback)
    timeout=45,  # default request timeout in seconds for every call; default is 30
)
```

`http2` is ignored when `transport` is also given, since a custom transport
owns its own protocol negotiation. `timeout` sets the client-wide default —
individual REST calls can still override it per-call via the lower-level
`RESTClientObject.request(..., timeout=...)`.

**Mutating requests (place/modify/cancel order) are never automatically
retried or replayed by the SDK.** `RESTClientObject.request()` makes exactly
one HTTP call per invocation — on a timeout or connection error it raises
immediately rather than resending, so an ambiguous failure (e.g. the broker
received the order but the response was lost) never risks a silent duplicate
order from client-side retry logic. The opt-in retry helpers in
`neo_api_client.retry` (see below) are not wired into `place_order`/
`modify_order`/`cancel_order` and must be applied explicitly by the caller if
wanted — and doing so for a mutating call is the caller's decision to make
with full awareness of the idempotency risk, not something the SDK does for you.

## Development

### Setup

```bash
# Clone repository
git clone https://github.com/Kotak-Neo/kotak-neo-python.git
cd kotak-neo-python

# Install dependencies
pip install -e ".[dev]"

# Setup pre-commit hooks
pre-commit install
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=neo_api_client --cov-report=html

# Run smoke tests (requires .env configuration)
python tests/e2e/smoke_test.py
```

> **SDK contributors:** the smoke/integration test runners can target an internal
> environment via the `NEO_ENVIRONMENT` variable. Ask an internal maintainer for
> the dev `.env` template for that setup. This is not needed by normal SDK users —
> the client always uses production by default.

### Code Quality

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Type checking
mypy neo_api_client

# Security scan
bandit -r neo_api_client
```

## Requirements

- **Python**: 3.10 or higher
- **Core Dependencies**: numpy, pandas, PyJWT, httpx[http2], websocket-client, structlog, tenacity, python-decouple, pyotp, websockets, pydantic

See [pyproject.toml](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/pyproject.toml) for complete dependency list.

## Repository Structure

```
kotak-neo-python/
├── neo_api_client/          # Main package
│   ├── services/            # API service modules
│   ├── websocket/           # WebSocket implementation
│   ├── utils/               # Utility functions
│   ├── neo_api.py          # Main NeoAPI class
│   ├── exceptions.py       # Exception hierarchy
│   └── ...                 # Core modules
├── tests/                   # Test suite
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── e2e/                # End-to-end tests
├── docs/                    # Documentation
│   ├── functions/          # API function docs
│   └── installation/       # Installation guides
└── pyproject.toml          # Project configuration
```

## Support

- **Documentation**: [GitHub Docs](https://github.com/Kotak-Neo/kotak-neo-python/tree/main/docs)
- **Issues**: [GitHub Issues](https://github.com/Kotak-Neo/kotak-neo-python/issues)
- **Email**: support@kotakneo.com

Reporting a bug? Enable file logging with `setup_logging(file_level="INFO")` (see the
[Logging Guide](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/docs/guides/logging.md)),
reproduce the issue, and attach the resulting `logs/neo-api-client.log` to your issue —
sensitive fields are already masked, so it's safe to share as-is.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see [LICENSE](https://github.com/Kotak-Neo/kotak-neo-python/blob/main/LICENSE) file for details.

## Disclaimer

This is the official SDK for Kotak Neo Trading APIs. Trading in financial markets involves substantial risk. Users are responsible for their own trading decisions and should thoroughly test their strategies before live trading.

**⚠️ Risk Warning**: As per SEBI study, 9 out of 10 individual traders in equity F&O segment incur net losses. Please trade responsibly.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

---

**Version**: 3.0.7  
**Status**: Production/Stable  
**Built with ❤️ by Kotak Neo Team**

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `neo_api_client/__version__.py`
```python
"""Version information for Neo API Client."""

__version__ = "3.0.7"
__version_info__ = tuple(int(i) for i in __version__.split("."))
```

#### File: `neo_api_client/services/__init__.py`
```python
"""
Internal service implementations.

Users should interact with the SDK through:

    from neo_api_client import NeoAPI

and not import service classes directly.
"""
```

#### File: `tests/unit/test_settings.py`
```python
"""Tests for settings module."""

from neo_api_client import settings


def test_settings_exchange_segment():
    """Test exchange segment settings."""
    assert "nse_cm" in settings.exchange_segment
    assert settings.exchange_segment["nse_cm"] == "nse_cm"


def test_settings_product():
    """Test product settings."""
    assert "CNC" in settings.product
    assert settings.product["CNC"] == "CNC"


def test_settings_order_type():
    """Test order type settings."""
    assert "L" in settings.order_type
    assert settings.order_type["L"] == "L"
```

#### File: `neo_api_client/websocket/feed/__init__.py`
```python
"""SFeed WebSocket client - Modern async/await implementation."""

from neo_api_client.websocket.feed.client import SFeedWebSocket
from neo_api_client.websocket.feed.models import (
    MARKET_STATUS_TEXT,
    DepthLevel,
    Exchange,
    Level,
    MarketStatusCode,
    SFeedCasChange,
    SFeedIndex,
    SFeedMarketStatus,
    SFeedScrip,
    SFeedScripLite,
    WsToken,
)

__all__ = [
    "SFeedWebSocket",
    "SFeedScrip",
    "SFeedScripLite",
    "SFeedIndex",
    "SFeedMarketStatus",
    "SFeedCasChange",
    "MarketStatusCode",
    "MARKET_STATUS_TEXT",
    "DepthLevel",
    "Exchange",
    "Level",
    "WsToken",
]
```

#### File: `neo_api_client/websocket/orderfeed/exceptions.py`
```python
"""Exceptions for the Order & Position streaming WebSocket client."""


class OrderFeedWebSocketError(Exception):
    """Base exception for Order Feed WebSocket errors."""

    pass


class ConnectionError(OrderFeedWebSocketError):
    """Raised when the WebSocket connection fails."""

    pass


class AuthenticationError(OrderFeedWebSocketError):
    """Raised when authentication fails."""

    pass


class AlreadyConnectedError(OrderFeedWebSocketError):
    """Raised when attempting to connect while already connected."""

    pass


class NotConnectedError(OrderFeedWebSocketError):
    """Raised when using the socket before it is connected."""

    pass
```


==================================================
