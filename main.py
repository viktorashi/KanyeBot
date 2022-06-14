import discord
# from discord.ext import commands
import os
import requests
import json
import random
# import openai
#sa tina serveru pornit
from keepalive import keep_alive

openaiToken = os.environ["openaiKey"]
discordToken= os.environ["discordKey"]
# my_secret = os.environ['openai']
# openai.api_key = mysecret

intents = discord.Intents.default()
#sa asculte comenzi
# client =  commands.Bot(command_prefix = 'fa ', intents = intents)
#sa asculte pt inceputuri de mesaj
client = discord.Client()

# async def completeCode(instruction, code,channel):
  # completie = #openai.Edit.create(
#   model="code-davinci-edit-001",
#   input=code,
#   instruction=instruction,
#   temperature=0.5
#   # top_p=1
# )
  # print(completie)
  # channel.send(completie["choices"][0]["text"])

# def completeaza(prompt):
#   completie = #openai.completion.create(
#         engine = "text-davinci-002",
#         prompt = prompt,
#         max_tokens = 720
#     )
#   print(completie)
#   return completie["choices"][0]["text"]



#comanda pe care-o folosesti (fa)
  
#seteaza comanda pe care o folosim




#ia quote de la kanye si intreaba ce ar zice marie curie la acest suicide note

#@client.command()

# def ai(prompt):
#   output = completeaza(prompt)
#   channel.send(output)
  

# async def pa(ctx):
#   quote = getKanyeQuote()
#   prompt = 'What the fuck did Kanye mean when he said: "' + quote + '"?\n'
#   print(quote)
#   await ctx.send(prompt)
#   await ctx.send("\n\n Phd. Armpit Musky, Reeboks dusty says: " + completeaza(prompt))
# #


####toate chestiile de kanye de aici
  
#iti dai tu seama
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
      
    #ca sa poti sa vb cu AI
    if message.content.lower().startswith('fa ai'):
      msg = message.content.split('fa ai')[1]
      print(msg)
      # await ai(msg, message.channel)
      

    # if message.content.lower().startswith('fa code'):
    #   msg = message.content.split('fa code')[1].split('\n')
    #   instructions = msg[0]
    #   code =  '\n'.join(msg[1:])
    #   print(msg)
    #   print(instructions)
    #   print(code)
    #   await completeCode(instructions,code,message.channel)
      
    # if message.content.lower().startswith('fa pa'):
    #   await pa(message.channel)

    if message.content.lower().startswith('fa cf'):
      await cf(message.channel)

    if message.content.lower().startswith('fa kanye'):
      await kanye(message.channel)
      
    if message.content.lower().startswith('fa ye'):
      await kanye(message.channel)

    if message.content.lower().startswith('fa sunt trist'):
      await sunt_trist(message.channel)
    if message.content.lower().startswith('fa sunt_trist'):
      await sunt_trist(message.channel)
    if message.content.lower().startswith('fa sunttrist'):
      await sunt_trist(message.channel)

    if message.content.lower().startswith('fa lista'):
      await lista(message.channel)

#nu
starter_encouragements = [
  "Las' frate ca are balta peste",
  "Macar nu est imai prost ca viktorel",
  "Sus barbia de Chad"
]

# options = starter_encouragements
# if "encouragements" in db.keys():
#  options = options + list (db["encouragements"])

#pt debugging
# print(db.keys())



# def update_enouragements (encouraging_message):
#   if "encouragements" in db.keys():
#     encouragements = db["encouragements"]
#     encouragements.append(encouraging_message)
#     db["encouragements"] = encouragements
#   else:
#     db["encouragements"] = [encouraging_message]

# def delete_encouragement(index):
#   if len(db["encouragements"]) - 1  > index:
#      del db["encouragements"][index]
#      return True
#   return False
  
#quoteuriile random
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

#quoturiile lu kanye specific
def getKanyeQuote():
  reponse = requests.get("https://api.kanye.rest")
  return json.loads(reponse.text)["quote"]

#comenzi care daca scrii in chat numele alea ale comenzilor se executa stii
#@client.command()
async def cf(ctx):
  await ctx.send("Ce faci coaie")

#@client.command()
async def kanye(ctx):
  await ctx.send(getKanyeQuote())


#@client.command()
async def sunt_trist(ctx):
 await ctx.send(random.choice(options))

#@client.command()
async def pl(ctx):
  await ctx.send('ce kkt vr')


  
# #@client.command()
# async def nou():
#   encouraging_message = msg.split("fa nou ",1)[1]
#   update_enouragements(encouraging_message)
#   await message.channel.send('Am pus "{}" in baza de date'.format(encouraging_message))

#@client.command()
async def lista(ctx):
  if "encouragements" in db.keys():
    await ctx.send(list(db["encouragements"]))
  else:
    await ctx.send("E goala baza de date coaie")



#trimite mesaj privat alora care dau join

@client.event
async def on_member_join(member):
  await member.send("Bine ai venit la noi in iadd coaie \n am fost trimis personal de owner sa-ti zic coaie")
  print("ceaw, "+ member)

@client.event
async def on_ready():
  print('Am efectual pula in cur! {0.user}'.format(client))


##pe astea le pastrez ca sa le dou intr-o buna zi refactor in metoda fara "starts with" stii ce zic
  
# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return

#   msg = message.content

#   options = starter_encouragements
#   if "encouragements" in db.keys():
#     options = options + list (db["encouragements"])

#   if msg.startswith('fa sunt trist'):
#       await message.channel.send(random.choice(options))
#       # await message.channel.send(get_quote() + "\n esti fericit acm?")
   
#   if msg.startswith("fa nou"):
#     encouraging_message = msg.split("fa nou ",1)[1]
#     update_enouragements(encouraging_message)
#     await message.channel.send('Am pus "{}" in baza de date'.format(encouraging_message))

#   if msg.startswith("fa sterge"):
#     encouragements = []
#     if "encouragements" in db.keys():
#       index = int(msg.split("fa sterge",1)[1])
#       if delete_encouragement(index):
#         encouragements = list(db["encouragements"])
#       else:
#         await message.channel.send("Hoo coaie ca nu am atatea mesaje")
#     await message.channel.send(encouragements)

#   if msg.startswith("fa lista"):
#     if "encouragements" in db.keys():
#        await message.channel.send(list(db["encouragements"]))
#     else:
#        await message.channel.send(db["E goala baza de date coaie"])

#   if any(word in msg for word in sad_words):
#     await message.channel.send(random.choice(starter_encouragements))
    

#run dat shit
  
keep_alive()
client.run(discordToken)
