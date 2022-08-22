import uuid

from main_console_app.data_base import all_numbers_cards

current_user_login = ""





def exit_user():
    global current_user_login
    if current_user_login != "":
        current_user_login = ""
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