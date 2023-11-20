from fastapi import FastAPI

import save_docs
from database import get_categories, get_menu_items, get_category
from models import Category

app = FastAPI()


@app.get("/")
async def get_root():
    """
    basic health check for the main route of the API.
    :return:JSON object with a single "state" key containing the string value "200 ok"
    """
    return {"state": "200 ok"}


@app.get("/categories")
async def get_all_categories_endpoint():
    """
    This fetches all category data from the database  .
    :return: The categories as a list of Category model objects serialized to JSON.
    """
    categories = get_categories()
    return [Category(**category) for category in categories]


@app.get("/category/{id_}")
async def get_category_endpoint(id_: int):
    """
    This fetch category data from the database by id .
    :param: id_: The id of the category ,
    :return: category information as a Category model objects serialized to JSON.
    """
    category_data = get_category(id_)
    return Category(**category_data[0]) if category_data else {"message": "Category not found"}


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

    save_docs.save()
    uvicorn.run("main:app", reload=True, app_dir="./",
                host="127.0.0.1", port=8080)
