import openai
import discord
import re
import os


# ----------# The following code relates to the OpenAI API configuration and communications

# OpenAI API token
openai.api_key =  os.getenv('OpenAIKey')

# Intial chatbot prompt
prompt = """The following is a conversation with an AI-powered Discord bot, a helpful, creative, clever, and very friendly AI assistant built for this Discord server. 
            The AI-powered Discord bot always responds in a professional tone and keeps things simple while prompting the user for further input. Keep responses concise and focused.
            \n\nHuman: Hello, who are you?\nAI: I am your AI-powered chatbot! I'm an AI here to help you out on this server. What can I do for you today? \nHuman: """

# Retrieves chatbot response from OpenAI API endpoint
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

# Loads the starting prompt into the chatbot
openai_create(prompt)



# ----------# The following code relates to the Discord API and handing discord bot functions

# Discord API Token
TOKEN =  os.getenv('DiscordAPIKey')

# Initializes the Discord client instance
client = discord.Client()


# Logs a confirmation message to the console when the bot is connected and ready.
@client.event
async def on_ready():
        print('Bot {0.user} is logged on and ready to go!'.format(client))


# Processe messages checking for command prefix
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
        
        #Logs the Name, Message and Channel of the message to the console
        print(f'{username}: {user_message} ({channel})')
    
        #Handels processing of the user message checking for "-gpt "
        if re.search("-gpt ", user_message): 
                str_list = user_message.split("-gpt ")
                UserPrompt = ""
                for element in str_list:
                        UserPrompt += element
                await message.channel.send(openai_create(UserPrompt))

# Starts discord bot
client.run(TOKEN)