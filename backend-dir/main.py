from models import *
from fastapi import FastAPI
from database import *

app = FastAPI()


@app.get("/")
async def get_root():
    """
    basic health check for the main route of the API.
    :return:JSON object with a single "state" key containing the string value "200 ok"
    """
    return {"state": "200 ok"}


@app.get("/categories")
async def get_categories_endpoint():
    """
    This fetches all category data from the database.
    This allows the frontend to easily display the list of all available main categories to the user.
    :return: the categories as a list of Category model objects serialized to JSON.
    """
    categories = get_categories()
    return [Category(**category) for category in categories]


@app.get("/menu")
async def get_menu_endpoint():
    """
    This endpoint fetches all menu item data from the database.
    This allows the frontend to display the list of all available menu items to build out the menu display for users.
    :return: It directly returns the list of menu items as a JSON array.
    """
    items = get_menu_items()
    return items


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, app_dir="./backend-dir",
                host="127.0.0.1", port=8080)
