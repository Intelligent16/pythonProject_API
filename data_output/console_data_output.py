import uuid
from data_input.console_data_input import get_avtoriz_data
from Authorization import check_login, check_password, users
from main_console_app.data_base import all_numbers_cards


current_user_login = ""


def avtorization():
    login, password = get_avtoriz_data()
    if not check_login(login):
        print("Такого пользователя не существует")
        return
    if not check_password(login, password):
        print("Неверный пользователь или пароль")
        return
    global current_user_login
    current_user_login = login
    # print("Привет,", login)
    print(f"Привет, {login}")


def print_current_user():
    global current_user_login
    if current_user_login != "":
        print(f"Пользователь: {current_user_login}")
    else:
        print("Вы не авторизированы")


def exit_user():
    global current_user_login
    if current_user_login != "":
        current_user_login = ""
        return

def registration():
    print("Регистрация")
    login, password = get_avtoriz_data()
    if login not in users:
        users[login] = password
        print("Регистрация успешна")
        global current_user_login
        current_user_login = login
    else:
        print("Такой пользователь уже существует")
        return

def is_autorise():
    global current_user_login
    if current_user_login != "":
        return True
    else:
        return False

def create_card():
    if is_autorise():
        number_card = generate_random_number_card()
        info_card = {"login": current_user_login, "balance": 0.0}
        all_numbers_cards[number_card] = info_card
    else:
        print("Пользоватлель не авторизован")

def generate_random_number_card():
    while True:
        number = str(uuid.uuid4())
        if number not in all_numbers_cards:
            return number

def print_all_card_info():
    for k in all_numbers_cards:
        print(k, all_numbers_cards[k])

def print_all_card_user():
    if is_autorise():
        global current_user_login
        for k in all_numbers_cards:
            if all_numbers_cards[k]["login"] == current_user_login:
                print(k, all_numbers_cards[k])