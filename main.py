import discord
# from discord.ext import commands
import os
import requests
import json
import random
import openai
#sa tina serveru pornit


openaiToken = os.environ["openaiKey"]
discordToken= os.environ["discordKey"]

openai.api_key = openaiToken

intents = discord.Intents.default()
#sa asculte comenzi
# client =  commands.Bot(command_prefix = 'fa ', intents = intents)
#sa asculte pt inceputuri de mesaj
client = discord.Client()

async def completeCode(instruction, code,channel):
  completie = openai.Edit.create(
  model="code-davinci-edit-001",
  input=code,
  instruction=instruction,
  temperature=0,
  top_p=1
)
  print(completie)
  await channel.send(completie["choices"][0]["text"])

def completeaza(prompt):
  completie = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        max_tokens = 300,
        temperature = 0.6,
        frequency_penalty=0,
        presence_penalty=0

    )
  print(completie)
  return completie["choices"][0]["text"]



#comanda pe care-o folosesti (fa)
  
#seteaza comanda pe care o folosim




#ia quote de la kanye si intreaba ce ar zice marie curie la acest suicide note

#@client.command()

async def ai(prompt, channel):
  output = completeaza(prompt)
  await channel.send(output)
  

async def pa(ctx):
  quote = getKanyeQuote()
  prompt = 'What the fuck did Kanye mean when he said: "' + quote + '"?\n'
  print(quote)
  await ctx.send(prompt)
  await ctx.send("\n\n Phd. Armpit Musky, Reeboks dusty says: " + completeaza(prompt))



####toate chestiile de kanye de aici
  
#iti dai tu seama
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

async def sunt_trist(channel):
  channel.send(get_quote()) 

@client.event
async def on_message(message):
    if message.author == client.user:
        return
      
      
    #ca sa poti sa vb cu AI
    if message.content.lower().startswith('fa ai'):
      msg = message.content.split('fa ai ' or "Fa ai ")[1]
      print(msg)
      output = completeaza(msg)
      await message.channel.send(output)
      

    if message.content.lower().startswith('fa code'):
      msg = message.content.lower().split('fa code ' or "Fa code ")[1].split('\n')
      instructions = msg[0]
      code =  '\n'.join(msg[1:])
      print(msg)
      print(instructions)
      print(code)
      await completeCode(instructions,code,message.channel)
      
    if message.content.lower().startswith('fa pa'):
      await pa(message.channel)

    if message.content.lower().startswith('fa cf'):
      await cf(message.channel)

    if message.content.lower().startswith('fa kanye'):
      await kanye(message.channel)
      
    if message.content.lower().startswith('fa ye'):
      await kanye(message.channel)
    
    if any(word in msg for word in sad_words):
      await sunt_trist(message.channel)

    if message.content.lower().startswith('fa sunt trist'):
      await sunt_trist(message.channel)
    if message.content.lower().startswith('fa sunt_trist'):
      await sunt_trist(message.channel)
    if message.content.lower().startswith('fa sunttrist'):
      await sunt_trist(message.channel)


    # if message.content.lower().startswith('fa lista'):
    #   await lista(message.channel)

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
  quote
  if(random.choice([0,1])):
    json_data =json.loads(requests.get("https://zenquotes.io/api/random").text) 
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
  else:
    response = random.choice(starter_encouragements)
  
  return quote

def getKanyeQuote():
  repose = requests.get("https://api.kanye.rest")
  json_data = json.loads(reponse.text)
  quote = "Kanye once said: \n" + json_data["quote"];
  return quote

@client.event
async def on_ready():
  print('Am efectual pula in cur! {0.user}'.format(client))


##pe astea le pastrez ca sa le dou intr-o buna zi refactor in metoda fara "starts with" stii ce zic
  

   
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


#run dat shit
  

client.run(discordToken)
