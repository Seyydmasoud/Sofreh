from fastapi import FastAPI, Query

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
@app.get("/C")
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


@app.get("/category/{cid}")
@app.get("/category")
@app.get("/c/{cid}")
async def get_category_endpoint(cid: int = 1):
    """
    This fetch category data from the database by id .
    :param cid: The id of the category .the default is 1 (even if not specified)
    :return: category information as a Category model objects serialized to JSON.
    """
    print(cid)
    category_data = get_category(cid)
    return Category(**category_data[0]) if category_data else {"message": f"Category not found by id={cid}"}


@app.get("/menu")
@app.get("/m")
async def get_menu_endpoint(limit: int = Query(default=10, le=100)):
    """
    This endpoint fetches a list of menu items from the database.

    This allows the frontend to display a list of menu items, and the `limit` query parameter
    can be used to control the number of items returned in the response.

    :param limit: The maximum number of items to return (default is 10, maximum is 100).
    :return: A JSON array containing menu items.
    """
    items = get_menu_items(limit=limit)
    if len(items) > 0:
        return [MenuItem(**item) for item in items]
    else:
        return {"message": "no MenuItem found"}


if __name__ == "__main__":
    import uvicorn

    save_docs.save()
    uvicorn.run("main:app", reload=True, app_dir="./",
                host="0.0.0.0", port=8080)
