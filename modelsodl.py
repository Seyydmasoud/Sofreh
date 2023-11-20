from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app = FastAPI()

users = {"tom": "1234"}


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})


@app.post("/login")
async def login(request: Request):
    form = dict(await request.form())

    username = form["username"]
    password = form["password"]
    if username in users and users[username] == password:
        context = {"request": request, "username": username}
        return templates.TemplateResponse("logged.html", context=context)

    else:
        context = {"request": request}
        return templates.TemplateResponse("errorLogin.html", context)


@app.get("/login")
async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
