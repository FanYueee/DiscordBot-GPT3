import discord
import openai
import time

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Settings
openai.api_key = ""
Discord_Bot_Token = ""
Discord_Channel_ID = ""


# Notification on console at startup
@client.event
async def on_ready():
    print(f"Successfully logged {client.user}")

# Main Program
@client.event
async def on_message(message):
    start_time = time.perf_counter()
    if message.author != client.user:
        if message.channel.id == int(Discord_Channel_ID):
            print("Send Request User:",message.author)
            print("Send Request Content:",message.content)
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=message.content,
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    temperature=0.5,
                )

                response = response["choices"][0]["text"]
                for i in range(0, len(response), 1000):
                    print("-------------------Content Start-------------------")
                    print(response[i:1000])
                    await message.channel.send(response[i:i + 1000])
                    end_time = time.perf_counter()
                print("-------------------Content End-------------------")
                print("Total Return Time:",round(end_time - start_time,2),"秒")
                print("-------------------Processing End-------------------")
            except:
                await message.channel.send("Oops! There seems to be no reverse transmission message")
                print("Oops! There seems to be no reverse transmission message")
                print("-------------------Processing End-------------------")

client.run(Discord_Bot_Token)
