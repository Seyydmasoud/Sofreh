FROM docker.arvancloud.ir/tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

WORKDIR /app
RUN echo "deb http://mirror.aminidc.com/debian bookworm main" > /etc/apt/sources.list
RUN rm /etc/apt/sources.list.d/debian.sources
COPY requirements.txt ./
RUN apt update && apt install -y libpq-dev gcc && rm -rf /var/cache/apt/*
RUN pip install -r requirements.txt

COPY ./app ./app

CMD [ "python", "/app/main.py" ]
