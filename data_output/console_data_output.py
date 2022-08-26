import uuid

from main_console_app.data_base import all_numbers_cards, current_user


def is_autorise():
    if current_user["user_name"] != "":
        return True
    else:
        return False


def generate_random_number_card():
    while True:
        number = str(uuid.uuid4())
        if number not in all_numbers_cards:
            return number
