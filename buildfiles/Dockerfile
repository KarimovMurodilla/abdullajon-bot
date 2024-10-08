FROM docker.io/python:3.11.7-slim-bookworm as python-base

# Install ffmpeg and other dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
ENV POETRY_VERSION=1.5.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache
    
FROM python-base as poetry-base

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

FROM python-base as app

COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app
COPY ../poetry.lock pyproject.toml ./
RUN mkdir -p /app/src/media/images/
RUN poetry check && \
    poetry install --no-interaction --no-cache --no-root

COPY .. .
CMD ["poetry", "run", "python", "-m", "src.bot"]
