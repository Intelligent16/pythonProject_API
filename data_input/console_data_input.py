from main_console_app.data_base import all_numbers_cards


def get_avtoriz_data():
    print("Укажите Ваш логин и пароль")
    login, password = input(), input()
    while login == "" or password == "":
        print("Укажите Ваш логин и пароль")
        login, password = input(), input()

    return login, password

def transfer_to_card():
    transfer_summ = check_transfer_summ()
    from_card = get_number_card("Вашей")
    to_card = get_number_card("другой")    all_tax = tax_of_transfer(transfer_summ)
    if transfer_summ + all_tax <= all_numbers_cards[from_card]["balance"]:
        all_numbers_cards[from_card]["balance"] = all_numbers_cards[from_card]["balance"] - transfer_summ - all_tax
        all_numbers_cards[to_card]["balance"] = all_numbers_cards[to_card]["balance"] + transfer_summ
    else:
        print("Недостаточно средств")

def get_number_card(message):
    while True:
        print(f"Введите номер {message} карты")
        number_card = input()
        if number_card != "" and number_card in all_numbers_cards:
            return number_card

def check_transfer_summ():
    while True:
        print("Введите сумму для перевода")
        transfer_summ = input()
        if transfer_summ.replace('.', '', 1).replace(',', '', 1).isdigit():
            transfer_summ = float(transfer_summ)
            if transfer_summ > 0:
                return transfer_summ

def tax_of_transfer(transfer_summ):
    tax = 0
    if transfer_summ < 1000:
        tax = 50
    elif 1000 <= transfer_summ < 10000:
        tax = transfer_summ * 0.02
    elif transfer_summ >= 10000:
        tax = transfer_summ * 0.01
    return tax