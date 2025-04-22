import discord
import json
import os
from dotenv import load_dotenv
import aiohttp
import logging

# Your Discord Bot Token
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
print(f"Token loaded: {DISCORD_TOKEN is not None}")

# Ollama API URL and headers
ollama_url = "http://host.docker.internal:11434/api/chat"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_API_KEY'  # If your API requires an API key
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
    combined_response = ""  # Initialize an empty string to hold the full response

    try:
        # Use aiohttp to send an asynchronous POST request to Ollama API
        async with aiohttp.ClientSession() as session:
            async with session.post(ollama_url, json=data, headers=headers) as response:
                if response.status != 200:
                    print(f"Error: {response.status}, {await response.text()}")
                    return None

                print("Response received from Ollama")  # Debug line
                # Stream response as chunks
                async for chunk in response.content.iter_any():
                    if chunk:  # Ensure the chunk is not empty
                        try:
                            # Decode and parse the chunk into JSON
                            chunk_data = chunk.decode("utf-8")
                            message_data = json.loads(chunk_data)

                            # Append the content of each chunk
                            if "message" in message_data and "content" in message_data["message"]:
                                combined_response += message_data["message"]["content"]

                            # Check if the response is complete
                            if message_data.get("done", False):
                                break  # End the loop when "done" is true

                        except json.JSONDecodeError as e:
                            print(f"Error decoding JSON chunk: {e}")
                            continue

        return combined_response

    except aiohttp.ClientError as e:
        print(f"Request Error: {e}")
        return None

# Event when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')  # Debug line

# Event when the bot receives a message
@client.event
async def on_message(message):
    print(f"Received message: {message.content}")  # Debug line

    # Don't let the bot respond to itself
    if message.author == client.user:
        return

    # Check if the message starts with !ask
    if message.content.startswith("!ask"):
        prompt = message.content[len("!ask "):]
        print(f"Received prompt: {prompt}")  # Debug line

        # Query the Ollama model for a response
        response = await query_ollama(prompt)  # Use await for async function

        if response:
            print(f"Response: {response}")  # Debug line
            await message.channel.send(response)
        else:
            await message.channel.send("Sorry, I couldn't process your request.")

# Start the bot
client.run(DISCORD_TOKEN)
