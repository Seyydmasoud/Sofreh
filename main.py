from fastapi import FastAPI
from database import get_categories, get_menu_items
from models import Category

app = FastAPI()


@app.get("/")
async def get_root():
    """
    basic health check for the main route of the API.
    :return:JSON object with a single "state" key containing the string value "200 ok"
    """
    return {"state": "200 ok"}


@app.get("/categories{category_ids}")
async def get_categories_endpoint(category_ids: list = None):
    """
    This fetches all category data from the database or specific categories by a list of IDs.
    :param category_ids: List of category IDs to filter the results.
    :return: The categories as a list of Category model objects serialized to JSON.
    """
    categories = get_categories(category_ids)
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

    uvicorn.run("main:app", reload=True, app_dir="./",
                host="127.0.0.1", port=8080)
