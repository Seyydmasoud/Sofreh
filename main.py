from fastapi import FastAPI

import save_docs
from database import get_categories, get_menu_items, get_category
from models import Category, MenuItem

app = FastAPI()


@app.get("/")
@app.get("/root")
async def get_root():
    """
    basic health check for the main route of the API.
    :return:JSON object with a single "state" key containing the string value "200 ok"
    """
    return {"state": "200 ok"}


@app.get("/categories")
@app.get("/c")
async def get_all_categories_endpoint():
    """
    This fetches all category data from the database  .
    :return: The categories as a list of Category model objects serialized to JSON.
    """
    categories = get_categories()
    if len(categories) > 0:
        return [Category(**category) for category in categories]
    else:
        return {"message": "no categories found"}


@app.get("/category/{id_}")
@app.get("/category")
@app.get("/c/{id_}")
async def get_category_endpoint(id_: int = 1):
    """
    This fetch category data from the database by id .
    :param: id_: The id of the category .the default is 1 (even if not specified)
    :return: category information as a Category model objects serialized to JSON.
    """
    category_data = get_category(id_)
    return Category(**category_data[0]) if category_data else {"message": f"Category not found by id={id_}"}


@app.get("/menu")
@app.get("/m")
async def get_menu_endpoint():
    """
    This endpoint fetches all menu item data from the database.
    This allows the frontend to display the list of all available menu items to build out the menu display for users.
    :return: It directly returns the list of menu items as a JSON array.
    """
    items = get_menu_items()
    if len(items) > 0:
        return [MenuItem(**item) for item in items]
    else:
        return {"message": "no categories found"}


if __name__ == "__main__":
    import uvicorn

    save_docs.save()
    uvicorn.run("main:app", reload=True, app_dir="./",
                host="127.0.0.1", port=8080)
