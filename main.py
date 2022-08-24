import sys

from fastapi import FastAPI

from Authorization import check_login, check_password
from data_input.console_data_input import tax_of_transfer, add_transaction_to_history
from data_output.console_data_output import is_autorise, generate_random_number_card
from main_console_app.data_base import users, current_user, all_numbers_cards, status_success, status_failed

import colorlog

logger = colorlog.getLogger('main')
logger.setLevel(colorlog.DEBUG)
stream_handler = colorlog.StreamHandler(stream=sys.stdout)
stream_handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s [%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S'))
logger.addHandler(stream_handler)
app = FastAPI()


@app.get("/")
async def print_all_comands():
    return


# todo
@app.post("/registration/{login}/{password}")
async def registration(login, password):
    logger.debug(f"pass: {password}, log: {login}")
    if login not in users:
        users[login] = password
        current_user["user_name"] = login
        logger.info("OK")
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


@app.post("/create_card")
def create_card():
    if is_autorise():
        number_card = generate_random_number_card()
        # todo
        info_card = {"login": current_user["user_name"], "balance": 0.0}
        all_numbers_cards[number_card] = info_card
        return {"message": "Карта создана успешно", "number_card": number_card}
    else:
        return {"message": "Пользоватлель не авторизован"}


@app.post("/exit_user")
def exit_user():
    if current_user["user_name"] != "":
        current_user["user_name"] = ""
        return {"message": "Вы не авторизованы"}


@app.get("/all_cards_info")
def get_all_cards_info():
    return all_numbers_cards


@app.get("/all_user_cards")
def get_all_cards_user():
    if is_autorise():
        user_cards = {}
        for k in all_numbers_cards:
            if all_numbers_cards[k]["login"] == current_user["user_name"]:
                user_cards[k] = all_numbers_cards[k]
        return user_cards
    else:
        return {"message": "Вы не авторизованы"}


@app.post("/transfer_to_card/{transfer_summ}/{from_card}/{to_card}")
def transfer_to_card(transfer_summ: float, from_card, to_card):
    # todo validation
    all_tax = tax_of_transfer(transfer_summ)
    if transfer_summ + all_tax <= all_numbers_cards[from_card]["balance"]:
        all_numbers_cards[from_card]["balance"] = all_numbers_cards[from_card]["balance"] - transfer_summ - all_tax
        all_numbers_cards[to_card]["balance"] = all_numbers_cards[to_card]["balance"] + transfer_summ
        add_transaction_to_history(all_tax, from_card, to_card, transfer_summ, status_success)
        return {"message": "Операция успешна"}
    else:
        add_transaction_to_history(all_tax, from_card, to_card, transfer_summ, status_failed)
        return {"message": "Недостаточно средств"}
