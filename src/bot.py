import discord
import json
import os
from dotenv import load_dotenv
import aiohttp
import logging

# Set up logging to help with debugging
logging.basicConfig(level=logging.DEBUG)

# Your Discord Bot Token
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
logging.info(f"Token loaded: {DISCORD_TOKEN is not None}")

# Ollama API URL and headers
ollama_url = "http://localhost:11434/api/chat"
headers = {
    'Content-Type': 'application/json'
}

# Initialize the client with intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure the bot can read message content
client = discord.Client(intents=intents)

# Asynchronous query to Ollama API
async def query_ollama(prompt):
    data = {
        "model": "openhermes",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(ollama_url, json=data, headers=headers) as response:
                if response.status != 200:
                    logging.error(f"Error: {response.status}, {await response.text()}")
                    return None
            
                result = await response.json()
                logging.debug(f"Ollama raw result: {json.dumps(result, indent=2)}")

                if "error" in result:
                    logging.error(f"Ollama error: {result['error']}")
                    return None

                return result.get("message", {}).get("content", "")

    except aiohttp.ClientError as e:
        logging.error(f"Request Error: {e}")
        return None

# Event when the bot is ready
@client.event
async def on_ready():
    logging.info(f'Logged in as {client.user}')

# Event when the bot receives a message
@client.event
async def on_message(message):
    logging.info(f"Received message: {message.content}")

    # Don't let the bot respond to itself
    if message.author == client.user:
        return

    # Check if the message starts with !ask
    if message.content.startswith("!ask"):
        prompt = message.content[len("!ask "):]

        # Check if the prompt is empty
        if not prompt:
            await message.channel.send("Please enter a prompt after `!ask`.")
            return
        
        logging.info(f"Received prompt: {prompt}")

        # Use a context manager to show typing status
        async with message.channel.typing():
            response = await query_ollama(prompt)

        if response and response.strip():
            logging.info(f"Response: {response}")
            await message.channel.send(response)
        else:
            logging.warning("Ollama returned an empty or invalid response.")
            await message.channel.send("Sorry, I couldn't process your request.")

# Start the bot
client.run(DISCORD_TOKEN)
