import os
import discord
import openai
from running import running

token = os.environ['DISCORD_TOKEN']
openai_key = os.environ['OPENAI_KEY']

openai.api_key = openai_key

intents = discord.Intents.all()
client = discord.Client(command_prefix='.', intents=intents)


# check if bot is running
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  # bot only responds to user
  if message.author == client.user:
    return
  
    
    # if you only want bot to respond when mentioned, add below line
  # if client.user in message.mentions:
    
    
    response = openai.Completion.create(
      engine = "text-davinci-003",
      prompt = f"{message.content}",
      max_tokens = 3000,
      temperature = 0.5)
    await message.channel.send(response.choices[0].text)

# keep bot perpetually running
running()

# run bot
client.run(token)
