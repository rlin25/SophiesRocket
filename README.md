# SophiesRocket

SophiesRocket is an AI-powered Discord chatbot built to interact with users in creative, intelligent, and fun ways. The bot is designed to be modular and easily extendable with features like LLM integrations, custom commands, and more.

## Features
- Responds to basic commands (`!ping`, `!help`)
- Easily extendable with AI integrations
- Customizable configuration for future updates

## Getting Started

### Prerequisites
- Python 3.10 or higher
- `pip` for installing dependencies
- A Discord Bot Token (see Discord Developer Portal setup below)
- [Ollama](https://ollama.com) for local LLM hosting

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/SophiesRocket.git
   cd SophiesRocket
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the bot**:
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

## Roadmap

- [x] Basic bot login and commands
- [ ] Add GPT-style AI responses via local model (text-generation-webui)
- [ ] Custom command framework for advanced bot interactions
- [ ] Webhook/API integration for external services

---

## License

MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgements

- [discord.py](https://github.com/Rapptz/discord.py) - Python wrapper for the Discord API
