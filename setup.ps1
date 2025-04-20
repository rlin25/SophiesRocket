Write-Host "Setting up SophiesRocket..." -ForegroundColor Cyan

# Check for Ollama
if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) {
    Write-Host "Ollama not found. Please install it from https://ollama.com/ and try again." -ForegroundColor Red
    exit 1
}

# Pull OpenHermes model
Write-Host "Pulling OpenHermes model with Ollama..." -ForegroundColor Yellow
ollama pull openhermes

# Optional: Set up Python virtual environment
if (Test-Path "requirements.txt") {
    Write-Host "Setting up Python virtual environment..." -ForegroundColor Yellow
    python -m venv venv

    .\venv\Scripts\Activate.ps1
    pip install -r requirements.txt
}
else {
    Write-Host "No requirements.txt found. Skipping Python setup." -ForegroundColor DarkGray
}

Write-Host "Setup complete!" -ForegroundColor Green
