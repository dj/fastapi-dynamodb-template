FROM python:3.11

WORKDIR /code

COPY pyproject.toml .
COPY setup_dev_db.py .
COPY .env .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3001", "--reload", "--reload-dir", "./app"]