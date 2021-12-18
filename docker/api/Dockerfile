FROM python:3.8-slim

WORKDIR /usr/src/server

RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]