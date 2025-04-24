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
    # Prepare data for the request (include the model in the payload)
    data = {
        "model": "openhermes",  # Add the model here
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        # Use aiohttp to send an asynchronous POST request to Ollama API
        async with aiohttp.ClientSession() as session:
            async with session.post(ollama_url, json=data, headers=headers) as response:
                if response.status != 200:
                    logging.error(f"Error: {response.status}, {await response.text()}")
                    return None

                logging.info("Response received from Ollama")  # Debug line
                # Get the full response directly (no chunking)
                response_data = await response.json()

                # Extract the message content
                if "message" in response_data and "content" in response_data["message"]:
                    return response_data["message"]["content"]

        return None

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
        logging.info(f"Received prompt: {prompt}")

        # Query the Ollama model for a response
        response = await query_ollama(prompt)  # Use await for async function

        if response and response.strip():
            logging.info(f"Response: {response}")
            await message.channel.send(response)
        else:
            logging.info("Response was empty or invalid")
            await message.channel.send("Sorry, I couldn't process your request.")

# Start the bot
client.run(DISCORD_TOKEN)
