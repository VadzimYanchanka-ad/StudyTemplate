FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY messenger ./messenger/

COPY pyproject.toml ./

RUN poetry config virtualenvs.create false \ 
    && poetry install --no-root

CMD ["poetry", "run", "uvicorn", "messenger.application.app:get_app", "--host", "0.0.0.0", "--port", "8000"]