from uuid import uuid4

from fastapi import FastAPI, Header

from Authorization import check_login, check_password, get_login_with_token
from data_input.console_data_input import tax_of_transfer, add_transaction_to_history
from data_output.console_data_output import is_autorise, generate_random_number_card
from main_console_app.data_base import users, all_numbers_cards, status_success, status_failed, \
    history_transactions, users_tokens
from models.models import LoginUserModel, RegistrationUserModel
from utils.logger import get_logger

logger = get_logger("main")

app = FastAPI()


@app.get("/")
async def print_all_comands():
    return


# todo
@app.post("/registration")
async def registration(user: RegistrationUserModel):
    logger.debug(f"pass: {user.password}, log: {user.login}")
    if user.login not in users:
        users[user.login] = user.password
        logger.info("OK")
        return {"message": "Регистрация успешна"}
    else:
        return {"message": "Такой пользователь уже существует"}


@app.post("/avtorization")
async def avtorization(user: LoginUserModel):
    if not check_login(user.login):
        return {"message": "Такого пользователя не существует"}
    if not check_password(user.login, user.password):
        return {"message": "Неверный пользователь или пароль"}
    token = str(uuid4())
    users_tokens[token] = user.login
    return {"message": f"Привет, {user.login}", "token": token}


@app.get("/current_user")
def get_current_user(authorization=Header(default=None)):
    if get_login_with_token(authorization) is not None:
        return {"current_user_name": users_tokens[authorization]}
    else:
        return {"message": "Вы не авторизированы"}


@app.post("/create_card")
def create_card(authorization=Header(default=None)):
    if is_autorise(authorization):
        number_card = generate_random_number_card()
        info_card = {"login": users_tokens[authorization], "balance": 0.0}
        all_numbers_cards[number_card] = info_card
        return {"message": "Карта создана успешно", "number_card": number_card}
    else:
        return {"message": "Пользоватлель не авторизован"}


@app.post("/logout")
def logout(authorization=Header(default=None)):
    del users_tokens[authorization]
    return {"message": "Вы вышли"}


@app.get("/all_cards_info")
def get_all_cards_info():
    return all_numbers_cards


# todo @app.get("/all_user_cards", dependencies=[Depends(HTTPBearer())])
@app.get("/all_user_cards")
def get_all_cards_user(authorization=Header(default=None)):
    if is_autorise(authorization):
        user_cards = {}
        for k in all_numbers_cards:
            if all_numbers_cards[k]["login"] == users_tokens[authorization]:
                user_cards[k] = all_numbers_cards[k]
        return user_cards
    else:
        return {"message": "Вы не авторизованы"}


@app.post("/transfer_to_card/{transfer_summ}/{from_card}/{to_card}")
def transfer_to_card(transfer_summ: float, from_card, to_card):
    # todo validation
    # todo is_autorise
    all_tax = tax_of_transfer(transfer_summ)
    if transfer_summ + all_tax <= all_numbers_cards[from_card]["balance"]:
        all_numbers_cards[from_card]["balance"] = all_numbers_cards[from_card]["balance"] - transfer_summ - all_tax
        all_numbers_cards[to_card]["balance"] = all_numbers_cards[to_card]["balance"] + transfer_summ
        add_transaction_to_history(all_tax, from_card, to_card, transfer_summ, status_success)
        return {"message": "Операция успешна"}
    else:
        add_transaction_to_history(all_tax, from_card, to_card, transfer_summ, status_failed)
        return {"message": "Недостаточно средств"}


@app.get("/history_of_transactions")
def get_history_transactions():
    return history_transactions
