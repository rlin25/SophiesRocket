# Development Log

### April 30, 2025 (Wednesday)
- Resolved Dockerfile dependency import issues.
- Upgraded Python version to 3.12.
- Restricted operations to virtual environment only.
- Refactored Dockerfile into multi-stage build:
  - Ensured only essential files are copied between stages.

### April 29, 2025 (Tuesday)
- Implemented cron job to prune unused Docker resources.
- Upgraded Poetry version:
  - Ensured Bash prioritizes `~/.local/bin`.

### April 28, 2025 (Monday)
- Fixed “remote unpack failed” error:
  - Removed `.venv` directory from GitHub history using BFG Repo-Cleaner.
- Linked GitHub repository to Jira.
- Migrated from `requirements.txt` to `pyproject.toml`:
  - Converted project into a Python package.
  - Replaced `discord.py` with `py-cord`.

### April 26, 2025 (Saturday)
- Connected `api.sophiesrocket.net` to the EC2 instance.
  - Allocated Elastic IP address.
- Registered domain: `www.fostermind.org`.

### April 25, 2025 (Friday)
- Downloaded OpenHermes 2.5 Mistral model:
  - Configured Hugging Face access token.
- Initialized SSH agent on AWS EC2.
- Migrated from Ollama to `llama-cpp-python`:
  - Updated Dockerfile and project dependencies.
- Resolved Discord error `50035: Invalid Form`:
  - Adjusted bot responses for clarity and brevity.

### April 24, 2025 (Thursday)
- Enabled SSH access to EC2 via Visual Studio Code.
- Resolved server error due to insufficient memory:
  - Upgraded EC2 instance to `t3.xlarge`.
- Fixed ghost message logic issue:
  - Removed Railway deployment.
- Allowed secure home access to project:
  - Updated EC2 Security Group rules.

### April 23, 2025 (Wednesday)
- Launched SophiesRocket instance on AWS EC2.
- Built Docker image:
  - Added user to Docker group.
- Deployed OpenHermes model with Ollama on EC2.
- Resolved 502 error (application non-responsive):
  - Reverted `ollama_url` to `localhost`.
  - Configured Docker to use host network.

### April 22, 2025 (Tuesday)
- Integrated GitHub Actions CI/CD pipeline:
  - Configured dependency caching.
  - Added secret: `DISCORD_TOKEN`.
- Deployed bot on Railway:
  - Refactored for asynchronous HTTP communication.
- Registered domain `www.sophiesrocket.net`:
  - Linked `api.sophiesrocket.net` to Railway.

### April 21, 2025 (Monday)
- Dockerized SophiesRocket application.
- Resolved API endpoint routing issue:
  - Updated Ollama URL to use Docker internal address.

### April 19, 2025 (Saturday)
- Logged development updates from April 18–19.
- Switched host to Ollama:
  - Loaded OpenHermes 2 Mistral model.
- Fixed JSON response splitting issue.
- Addressed Discord token exposure:
  - Attempted rebase to remove sensitive history.
- Implemented workaround for missing response package:
  - Created virtual environment.
- Conducted Discord-based prompt testing.

### April 18, 2025 (Friday)
- Enabled OpenAI-compatible API:
  - Verified connection using `curl`.
- Configured `setup.sh`.
- Set up Discord bot:
  - Configured application via [Discord Developer Portal](https://discord.com/developers/applications).
  - Secured token in `.env` file.
  - Enabled necessary **Privileged Gateway Intents**.
- Tested Discord integration:
  - Invited bot using OAuth2.
  - Logged in as **SophiesRocket#3384**.
  - Confirmed successful interaction.

### April 17, 2025 (Thursday)
- Deployed GPU instance via RunPod:
  - Specs: 3× RTX 4090.
  - Template: Text Generation WebUI.
- Loaded OpenHermes Mixtral model:
  - Source: TheBloke/OpenHermes-2.5-Mistral-7B-GGUF.
  - Format: `openhermes-2.5-mistral-7b.Q5_K_M.gguf`.