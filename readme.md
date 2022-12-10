# OpenAI Chat DiscordBot
[繁體中文](https://github.com/FanYueee/OpenAI-Chat-Discord-Bot/blob/main/readme_zh.md)

An AI interactive robot that runs on OpenAI and is connected to Discord.
Only messages sent in the specified Discord channel are sent to OpenAI and the returned data is sent to that channel, the rest of the channels are ignored.

Each OpenAI account has a trial balance of 18 USD for three months, which is already available when you create an account, no need to apply for additional, this robot will cost the balance please note!!!
## Must library
Only represents the version used during development. It does not mean that other versions cannot be deployed.

| Library | Version |
|-------------|---------|
| discord.py  | 2.1.0   |
| openai      | 0.25.0  |

## Settings
[OpenAI-Chat-Discord-Bot/main.py](https://github.com/FanYueee/OpenAI-Chat-Discord-Bot/blob/main/main.py)
```py
openai.api_key = ""
Discord_Bot_Token = ""
Discord_Channel_ID = ""
```
### openai.api_key
Can be generated at https://beta.openai.com/account/api-keys and copied here
### Discord_Bot_Token
Discord Bot Token https://discord.com/developers/applications
### Discord_Channel_ID
Sending a request to OpenAI will only be sent if the message is in the specified channel.
