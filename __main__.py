import discord, json, asyncio

GUILDS = None

startAtTestingMode = input("Should I start in DEBUG MODE (y/n) >>> ")
if startAtTestingMode == "y":
    GUILDS = json.load(open("botConfig.json", "r"))["GUILDS"]

intents = discord.Intents.all()

client = discord.Bot(intents=intents)
token = json.load(open("botConfig.json", "r"))["TOKEN"]
print("Starting up the bot...")

@client.event
async def on_ready():
    if startAtTestingMode == "y":
        print("[DEBUG MODE]: Enabled.")
    else:
        print("[DEBUG MODE]: Disabled.")
    print("[BOT]: Started and now are ready!")

from CarryBot.Commands.createCarry import createCarryCommand
createCarryCommand(client, GUILDS)

client.run(token)
