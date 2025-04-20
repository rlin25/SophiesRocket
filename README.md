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

### Clone the repository

```bash
git clone https://github.com/yourusername/SophiesRocket.git
cd SophiesRocket
```

### Windows (PowerShell)

Open **PowerShell** and run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
./setup.ps1
```

## Running the Bot
   ```bash
   python bot.py
   ```

---

## Discord Developer Setup

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **"New Application"** and name it `SophiesRocket`.
3. Under the **Bot** tab:
   - Click **"Add Bot"**
   - Enable **MESSAGE CONTENT INTENT** and other necessary intents.
4. Under **OAuth2 > URL Generator**:
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
