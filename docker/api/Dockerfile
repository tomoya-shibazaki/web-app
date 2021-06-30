FROM python:3.9

WORKDIR /usr/src/server
COPY Pipfile .
RUN pipenv install
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]