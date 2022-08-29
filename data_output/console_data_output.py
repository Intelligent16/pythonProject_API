import uuid

from Authorization import get_login_with_token
from main_console_app.data_base import all_numbers_cards


def is_autorise(authorization):
    return get_login_with_token(authorization) is not None


def generate_random_number_card():
    while True:
        number = str(uuid.uuid4())
        if number not in all_numbers_cards:
            return number
