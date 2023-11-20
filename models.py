from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str
    description: str
    image_url: str


class Subcategory(BaseModel):
    id: int
    name: str
    description: str
    image_url: str
    parent_id: int


class Menu(BaseModel):
    id: int
    name: str
    description: str
    price: int
    discount: float
    category_id: int


class MenuImage(BaseModel):
    id: int
    menu_item_id: int
    image_url: str


class User(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    address: str
    city: str
    state: str
    zip_code: str


class Order(BaseModel):
    id: int
    user_id: int
    address: str
    total_price: int
    status: str


class OrderDetail(BaseModel):
    id: int
    order_id: int
    menu_item_id: int
    quantity: int


class MenuItem(BaseModel):
    id: int
    name: str
    price: float
    category_id: int
