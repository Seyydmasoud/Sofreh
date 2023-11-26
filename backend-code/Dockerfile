FROM docker.arvancloud.ir/python:3.11.6-alpine3.18

WORKDIR /app
COPY requirements.txt ./
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt

COPY . .
CMD [ "python", "/app/main.py" ]
