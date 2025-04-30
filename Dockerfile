# ===== Stage 1: Builder =====
FROM python:3.12-slim AS builder

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

# Configure Poetry to put the venv inside the project directory
RUN poetry config virtualenvs.in-project true

# Copy project files
COPY . /app

# Install dependencies (creates /app/.venv)
RUN poetry install --no-interaction --no-ansi

# ===== Stage 2: Runtime =====
FROM python:3.12-slim

WORKDIR /app

# Install minimal runtime dependencies
RUN apt-get update && apt-get install -y \
    libstdc++6 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy only the necessary files from the builder stage
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/models /app/models
COPY --from=builder /app/src /app/src
COPY --from=builder /app/pyproject.toml /app/
COPY --from=builder /app/poetry.lock /app/

# Ensure the virtual environment is used
ENV PATH="/app/.venv/bin:$PATH"

# Run using the Python interpreter from the virtual environment
CMD ["/app/.venv/bin/python", "src/sophiesrocket/bot.py"]