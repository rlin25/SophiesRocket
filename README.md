# Sophie's Rocket

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Discord](https://img.shields.io/badge/Discord-7289DA?style=flat&logo=discord&logoColor=white)](https://discord.com)

A Discord chatbot powered by OpenHermes-2.5-Mistral-7B, bringing AI conversations to your server.

</div>

## Features

- **Local LLM Integration**: Powered by OpenHermes-2.5-Mistral-7B via llama-cpp-python
- **Real-time Responses**: Asynchronous message handling with concurrent processing
- **Message Filtering**: Responds to `!ask` command prefix
- **Detailed Logging**: Comprehensive debug logging for troubleshooting
- **Environment Variables**: Secure token management with python-dotenv
- **Performance Optimized**: Thread pool executor for efficient LLM inference

## Prerequisites

- Python 3.12 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- Discord Bot Token
- OpenHermes-2.5-Mistral-7B model file (Q5_K_M quantized)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SophiesRocket.git
cd SophiesRocket
```

### 2. Install Dependencies

```bash
poetry install
```

### 3. Configure Environment

Create a `.env` file in the root directory:

```env
DISCORD_TOKEN=your_discord_bot_token
```

### 4. Download Model

Place the OpenHermes model file at `models/openhermes-2.5-mistral-7b.Q5_K_M.gguf`

### 5. Run the Bot

```bash
poetry run python -m sophiesrocket.bot
```

## Bot Usage

The bot responds to messages starting with `!ask`. For example:
```
!ask What is the capital of France?
```

## Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `DISCORD_TOKEN` | Discord bot token | Yes | - |

### Model Configuration

The bot uses the following model settings:
- Context window: 2048 tokens
- Max output tokens: 500
- Model: OpenHermes-2.5-Mistral-7B (Q5_K_M quantized)

## Project Structure

```
src/sophiesrocket/
├── __init__.py
├── bot.py      # Main Discord bot implementation
│   ├── Discord client setup
│   ├── Message handling
│   └── LLM integration
└── llm.py      # LLM query implementation
    └── Health check functionality
```

## Code Flow

1. **Initialization**:
   - Load environment variables
   - Initialize Llama model
   - Configure Discord intents
   - Set up thread pool executor

2. **Message Processing**:
   - Listen for messages
   - Filter for `!ask` prefix
   - Extract prompt from message
   - Show typing indicator

3. **LLM Integration**:
   - Run inference in separate thread
   - Process model output
   - Handle response formatting
   - Send response to Discord

4. **Error Handling**:
   - Log all operations
   - Handle model errors
   - Manage thread execution
   - Provide user feedback

## Docker Support

### Build the Image

```bash
docker build -t sophiesrocket .
```

### Run the Container

```bash
docker run --rm --env-file .env sophiesrocket
```

## Dependencies

- py-cord (≥2.3.0)
- python-dotenv (≥1.0.0)
- requests (≥2.32.3)
- aiohttp
- llama-cpp-python
- numpy (≥1.26.0)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [py-cord](https://github.com/Pycord-Development/pycord) - Discord API wrapper
- [OpenHermes-2.5-Mistral-7B](https://huggingface.co/OpenHermes) - LLM model
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) - LLM inference

---

<div align="center">
Made with ❤️ by Richard Lin
</div>
