from fastapi import FastAPI

from Authorization import check_login, check_password
from main_console_app.data_base import users, current_user

app = FastAPI()


@app.get("/")
async def print_all_comands():
    return


# todo
@app.post("/registration/{login}/{password}")
async def registration(login, password):
    if login not in users:
        users[login] = password
        current_user["user_name"] = login
        return {"message": "Регистрация успешна"}
    else:
        return {"message": "Такой пользователь уже существует"}


@app.post("/avtorization/{login}/{password}")
async def avtorization(login, password):
    if not check_login(login):
        return {"message": "Такого пользователя не существует"}
    if not check_password(login, password):
        return {"message": "Неверный пользователь или пароль"}
    current_user["user_name"] = login
    return {"message": f"Привет, {login}"}


@app.get("/current_user")
def get_current_user():
    if current_user["user_name"] != "":
        return {"current_user_name": current_user["user_name"]}
    else:
        return {"message": "Вы не авторизированы"}
