from main_console_app.data_base import all_numbers_cards


def get_avtoriz_data():
    print("Укажите Ваш логин и пароль")
    login, password = input(), input()
    while login == "" or password == "":
        print("Укажите Ваш логин и пароль")
        login, password = input(), input()

    return login, password

def transfer_to_card():
    transfer_summ = float(input())
    from_card = input()
    to_card = input()
    all_numbers_cards[from_card]["balance"] = all_numbers_cards[from_card]["balance"] - transfer_summ
    all_numbers_cards[to_card]["balance"] = all_numbers_cards[to_card]["balance"] + transfer_summ


