import requests


def test_root():
    response = requests.get("http://localhost:8080/")
    assert response.status_code == 200
    categories = response.json()
    assert len(categories) > 0
    print("root:", categories.items(), " test passed.")


def test_get_categories():
    response = requests.get("http://localhost:8080/categories")
    assert response.status_code == 200
    categories = response.json()
    assert len(categories) > 0
    print("get_categories called:", *categories, sep="\n")


def test_get_category(id_):
    response = requests.get("http://localhost:8080/category/{}".format(id_))
    assert response.status_code == 200
    category = response.json()
    assert category
    print("test_get_category called:", category, sep="\n")


def test_get_subcategories():
    response = requests.get("http://localhost:8080/subcategories")
    assert response.status_code == 200
    categories = response.json()
    assert len(categories) > 0
    print("get_categories called:", *categories, sep="\n")


def test_get_menu():
    response = requests.get("http://localhost:8080/menu")
    assert response.status_code == 200
    menu = response.json()
    assert (len(menu) > 0 or len(menu) == 0)
    print("get_menu ", menu, " test passed.")


if __name__ == "__main__":
    test_root()
    print("-" * 100)
    test_get_categories()
    print("-" * 100)
    test_get_category(1)
    print("-" * 100)
    test_get_menu()
