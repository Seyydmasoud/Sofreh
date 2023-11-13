from models import *
from fastapi import FastAPI
from database import *

app = FastAPI()


@app.get("/")
async def get_root():
    return {"state": "200 ok"}


@app.get("/categories")
async def get_categories_endpoint():
    categories = get_categories()
    return [Category(**category) for category in categories]


@app.get("/menu")
async def get_menu_endpoint():
    items = get_menu_items()
    return items


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, app_dir="./backend-dir",
                host="127.0.0.1", port=8080)
