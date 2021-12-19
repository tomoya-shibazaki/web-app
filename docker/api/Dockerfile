FROM python:3.8.7-slim

    # python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    POETRY_VERSION=1.1.12

# System deps:
RUN pip install --upgrade pip && pip install "poetry==$POETRY_VERSION"

WORKDIR /usr/src/server

RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev

COPY poetry.lock pyproject.toml ./

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]