# OpenAI Chat DiscordBot
一個藉由 OpenAI 所運行的 AI 互動機器人，並將其連接至 Discord 上。
在指定 Discord 頻道內所發送的訊息才會傳到 OpenAI 內，並將回傳的資料到該頻道，其餘頻道都不會理會。

每個 OpenAI 帳號都擁有三個月 18 美金的試用餘額，創建帳號時就已經擁有，無須額外申請，這個機器人會花費餘額請注意!!!
## 必須函式庫
僅代表開發時使用版本，不代表其他版本無法部署。

| 名稱         | 版本     |
|------------|--------|
| discord.py | 2.1.0  |
| openai     | 0.25.0 |

## 設定
[OpenAI-Chat-Discord-Bot/main.py](https://github.com/FanYueee/OpenAI-Chat-Discord-Bot/blob/main/main.py)
```py
openai.api_key = ""
Discord_Bot_Token = ""
Discord_Channel_ID = ""
```
### openai.api_key
可於 https://beta.openai.com/account/api-keys 生成，並將其複製至此處
### Discord_Bot_Token
Discord Bot Token https://discord.com/developers/applications
### Discord_Channel_ID
指定於哪一個頻道發送的訊息才會運行本機器人
