import os
import discord
import requests
import json
import random 

token = os.environ['token']
client = discord.Client()

sad_words = ["trist", "depresiv", "prost", "mor" , "moarte", "n-am chef", "mizerabil", "depressing", "depressed", "fucking", "fucking die"]

starter_encouregements = [
  "Hai coaie sus maxilaru ala de Chad",
  "Ba, macar nu esti la fel de prost ca Viktor, asa-i coaie?",
  "Esti cel mai forta om/robot =)))) smr ce codar prst m-a fct"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print("Da coaie, {0.user}".format(client), "sunt in viata, cce faci?")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if msg.startswith("fa sunt trist"):
    await message.channel.send(get_quote() + "\n gata, mai fericit? (da/nu)")
    # if await message.conent.startswith("nu"):
    #    await message.channel.send("Atunci dute-n mortii matii")
    # elif await message.conent.startswith("da"):
    #    await message.channel.send("Cu placere in mortii tai")
  elif msg.startswith("fa"):  
    await message.channel.send("Uhh dute-n mortii mati")
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouregements))


client.run(token)