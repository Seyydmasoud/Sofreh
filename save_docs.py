from fastapi import FastAPI
from main import app
import json


def save():
    openapi_schema = app.openapi()
    with open('openapi_schema.json', 'w') as file:
        json.dump(openapi_schema, file)
