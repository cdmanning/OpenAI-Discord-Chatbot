import openai
import discord
import re


# ----------# The following code relates to the ChatGPT language model hosted and provided by OpenAI through the API Token.

# OpenAI API Token
key =  os.getenv('OpenAIKey')

openai.api_key = key


# Intial OpenAI chatbot prompt
prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "


# Function that takes in a prompt for the API and resturns the chatbot's responce
def openai_create(prompt):
        response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
        )
        return response.choices[0].text


# Initializes the OpenAI chatbot with the initial prompt
openai_create(prompt)


# ----------# The following code relates to the Discord API and handing discord bot functions

# Discord API Token
TOKEN =  os.getenv('DiscordAPIKey')

# Declares the client variable for the discord client
client = discord.Client()


# Sends a serverside message when the bot is ready
@client.event
async def on_ready():
        print('Bot {0.user} is logged on and ready to go!'.format(client))


# on_message client event checks each message sent in the discord chat
@client.event
async def on_message(message):
        
        
        #Prevents looping of the bot responding to itself
        if message.author == client.user:
                return


        # Retreives the username/author for the message sent in chat
        username = str(message.author).split('#')[0]


        # Retreives the contents of the message sent in chat
        user_message = str(message.content)


        # Retreives the name of the channel that the message was sent in
        channel = str(message.channel.name)
        
        
        #Prints to the clientside console the Name, Message and Channel of the message that was processed
        print(f'{username}: {user_message} ({channel})')
    
    
        #Handels processing of the user message checking for "-gpt "
        if re.search("-gpt ", user_message):
                
                str_list = user_message.split("-gpt ")
                UserPrompt = ""
                for element in str_list:
                        UserPrompt += element
                await message.channel.send(openai_create(UserPrompt))


# Begins running the discord bot client using the API Token
client.run(TOKEN)
