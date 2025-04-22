# Development Log

## 2025, April 22

## 2025, April 21
- Dockerize SophiesRocket
- Resolved issue with API endpoint
  - Updated Ollama url to internal docker address

## 2025, April 19
- Record `dev-log.md` updates for 4/18 - 4/19
- Change host to Ollama
  - Load OpenHermes 2 Mistral model
- Fix split JSON response error
- Resolve Discord token exposure
  - Attempt rebase of vulnerable file version
- Work around missing response package
  - Create virtual environment
- Test basic questions via Discord

## 2025, April 18
- Enable OpenAI-Compatible API
  - Test Connection using curl
- Configure setup.sh
- Setup Discord Bot
  - Set configuration via [Discord Developer Portal](https://discord.com/developers/applications)
  - Stored Discord bot token in `.env` file
  - Set required **Privileged Gateway Intents**
- Test Discord Connection
  - Invite bot to custom server using OAuth2
  - Log in as **SophiesRocket#3384** successfully.
  - Received positive response

## 2025, April 17
- Setup GPU RunPod instance
  - GPU: x3 RTX 4090
  - Template: Text Generation WebUI
- Load OpenHermes Mixtral model
  - Source: TheBloke/OpenHermes-2.5-Mistral-7B-GGUF
  - Model: openhermes-2.5-mistral-7b.Q5_K_M.gguf
