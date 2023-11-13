import psycopg2

from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    database="sofrehdb",
    user="postgres",
    password="password",
    host='localhost',
    port='5432'
)


def get_categories():
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        query = (" SELECT *"
                 " FROM categories"
                 " WHERE id<=10")
        cursor.execute(query)
        categories = cursor.fetchall()
        return categories

    except Exception as error:
        return {"Error: ", error}


def get_menu_items(limit=10):
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        query = (" SELECT *"
                 " FROM categories"
                 f" WHERE id<={limit}")
        cursor.execute(query)
        items = cursor.fetchall()
        return items
    except Exception as error:
        return {"Error: ", error}
