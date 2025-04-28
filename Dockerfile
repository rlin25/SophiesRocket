FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install build tools and dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    python3-dev \
    git \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry (official way)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to the PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy all files first
COPY . /app

# Install dependencies
RUN poetry install \
    && pip install py-cord \
    && pip install dotenv \
    && pip install llama-cpp-python

# Run the bot
CMD ["python3", "src/sophiesrocket/bot.py"]
