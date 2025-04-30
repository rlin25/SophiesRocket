# SophiesRocket

SophiesRocket is an AI-powered Discord chatbot powered by OpenHermes via Ollama. It is built to interact with users in creative, intelligent, and fun ways.

## Features

- Uses [Ollama](https://ollama.com/) to run local LLMs
- Streams replies from the OpenHermes model
- Easily customizable for your own Discord bot logic

## Getting Started

### Prerequisites
- [Python 3.10](https://www.python.org/) or higher
- [Ollama](https://ollama.com) for local LLM hosting  
- A Discord Bot Token (see [Discord Developer Portal](https://discord.com/developers/applications) setup below)


## Quick Start

### Docker Setup

#### 1. Build the Docker image

First, build the Docker image:

```bash
docker build --progress=plain -t sophiesrocket .
```

#### 2. Run the Docker container

Once the image is built, run the container:

```bash
docker run --rm --detach --network=host --env-file .env -v $(pwd)/.venv:/app/.venv sophiesrocket
```

- This runs the Docker container with the environment variables specified in `.env`, uses the host's network, sets up a persistent .venv volume, and starts the bot

---

## Discord Developer Setup

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **"New Application"** and name it `SophiesRocket`.
3. In the sidebar, go to **"Bot"** → click **"Add Bot"** → confirm.
4. Under **Token**, click **"Reset Token"** → **Copy** the token.
    - Store the value in .env as `DISCORD_TOKEN`
    - **Keep this token secret**. Never commit it to GitHub.
5. Under **OAuth2 > URL Generator**:
    - Select **bot** scope
    - Choose permissions like: `Read Messages`, `Send Messages`, `Embed Links`, `Use Slash Commands`
    - Copy the generated URL and invite the bot to your server with appropriate permissions.

---

## License

MIT License. See the [LICENSE](LICENSE.md) file for more details.

---

## Acknowledgements

- [discord.py](https://github.com/Rapptz/discord.py) - Python wrapper for the Discord API
- [OpenHermes](https://huggingface.co/OpenHermes) - General purpose LLM model
