import discord

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# Place your bot token here
BOT_TOKEN = 'YOUR_BOT_TOKEN'

async def send_hello_world(channel):
    try:
        await channel.send('Hello, world!')
    except Exception as e:
        print(f"Error sending message: {e}")

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions and 'general' in str(message.channel):
        channel = message.channel
        task = client.loop.create_task(send_hello_world(channel))
        await task

async def start_bot():
    await client.start(BOT_TOKEN)

# Run the bot using asyncio in a Jupyter Notebook
import nest_asyncio
nest_asyncio.apply()
import asyncio

async def run_bot():
    await start_bot()

loop = asyncio.get_event_loop()
loop.run_until_complete(run_bot())

# To stop the bot later (optional)
# client.close()
# loop.run_until_complete(client.logout())
