FROM python:3.12.6-slim

ENV POETRY_VERSION=1.8.4 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir poetry==${POETRY_VERSION} \
    && poetry --version \
    && poetry install --no-root

EXPOSE 80

CMD poetry run alembic -c alembic/alembic.ini upgrade head && poetry run python main.py
