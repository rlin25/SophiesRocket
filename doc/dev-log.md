# Development Log

## 2025, April 26, Saturday
- Connect api.sophiesrocket.net to sophiesrocket-instance
  - Allocate elastic IP address
- Register www.fostermind.org

## 2025, April 25, Friday
- Wget OpenHermes 2.5 Mistral
  - Setup Hugging Face access token
- Start SSH agent on AWS EC2
- Switch from Ollama to llama-cpp-python
  - Adjust Dockerfile, requirements
- Resolve 50035 error: Invalid Form
  - Prompt SophiesRocket to be concise

## 2025, April 24, Thursday
- SSH into AWS EC2 from Visual Studio Code
- Resolve 500 error: model requires more system memory
  - Upgrade EC2 Instance to t3.xlarge
- Solve ghost message logic error
  - Delete Railway deployment
- Allow project access from home
  - Update AWS EC2 Security Groups

## 2025, April 23, Wednesday
- Launch SophiesRocket-Instance on AWS EC2
- Build Docker image
  - Add user to Docker group
- Run Ollama with OpenHermes on AWS EC2
- Resolve 502 error: application failed to respond
  - Reverted `ollama_url` to localhost address
  - Set Docker image to run on host machine's network stack

## 2025, April 22, Tuesday
- Integrate GitHub Actions
  - Setup cached dependencies
  - Add secret `DISCORD_TOKEN`
- Deploy bot on Railway
  - Refactor for asynchronous HTTP requests
- Register www.sophiesrocket.net
  - Connect api.sophiesrocket.net to Railway

## 2025, April 21, Monday
- Dockerize SophiesRocket
- Resolve issue with API endpoint
  - Update Ollama URL to internal docker address

## 2025, April 19, Saturday
- Record `dev-log.md` updates for 4/18 - 4/19
- Change host to Ollama
  - Load OpenHermes 2 Mistral model
- Fix split JSON response error
- Resolve Discord token exposure
  - Attempt rebase of vulnerable file version
- Work around missing response package
  - Create virtual environment
- Test basic questions via Discord

## 2025, April 18, Friday
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

## 2025, April 17, Thursday
- Setup GPU RunPod instance
  - GPU: x3 RTX 4090
  - Template: Text Generation WebUI
- Load OpenHermes Mixtral model
  - Source: TheBloke/OpenHermes-2.5-Mistral-7B-GGUF
  - Model: openhermes-2.5-mistral-7b.Q5_K_M.gguf
