import discord
import json
import os
from dotenv import load_dotenv
import logging
import concurrent.futures
import asyncio
import time

from llama_cpp import Llama

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Path to the OpenHermes model file
MODEL_PATH = "models/openhermes-2.5-mistral-7b.Q5_K_M.gguf"  # Update this if needed

# Initialize the Llama model
logging.info("Initializing Llama model...")
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)
logging.info("Llama model initialized.")

# Create a thread pool executor for Llama inference
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

# Initialize the Discord client with message intent
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Query function using llama-cpp (run in a separate thread)
async def query_llama_in_thread(prompt):
    loop = asyncio.get_event_loop()
    try:
        logging.info("Sending query to Llama model...")
        start_time = time.time()
        result = await loop.run_in_executor(executor, query_llama, prompt)
        end_time = time.time()
        logging.info(f"Llama query completed in {end_time - start_time:.2f} seconds.")
        return result
    except Exception as e:
        logging.error(f"Error running query in thread: {e}")
        return None

# Function to query the Llama model
def query_llama(prompt):
    try:
        logging.info("Running prompt through Llama...")

        # Modify the prompt to ask for a concise response
        concise_prompt = f"Please provide a concise answer to the following question: {prompt}"
        
        output = llm(
            prompt,
            max_tokens=512,
            stop=["</s>"],
            echo=False
        )
        
        if not output:
            logging.error("No output returned from Llama.")
            return None

        logging.debug(f"Llama output: {json.dumps(output, indent=2)}")
        return output["choices"][0]["text"].strip()
    except Exception as e:
        logging.error(f"Llama Error: {e}")
        return None

# Event: bot is ready
@client.event
async def on_ready():
    logging.info(f'Logged in as {client.user}')

# Event: message received
@client.event
async def on_message(message):
    logging.info(f"Received message: {message.content}")

    if message.author == client.user:
        return

    if message.content.startswith("!ask"):
        prompt = message.content[len("!ask "):].strip()

        if not prompt:
            await message.channel.send("Please enter a prompt after `!ask`.")
            return

        logging.info(f"Prompt: {prompt}")

        async with message.channel.typing():
            response = await query_llama_in_thread(prompt)

        if response:
            logging.info(f"Response: {response}")
            await message.channel.send(response)
        else:
            await message.channel.send("Sorry, I couldn't process your request.")

# Start the bot
client.run(DISCORD_TOKEN)
