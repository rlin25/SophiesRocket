FROM python:3.11-slim

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    python3-dev \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

# Copy all project files first (including src/)
COPY . /app

# Disable virtualenv creation
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi \
    && pip install py-cord \
    && pip install dotenv \
    && pip install llama-cpp-python

# Run the bot
CMD ["python3", "src/sophiesrocket/bot.py"]
