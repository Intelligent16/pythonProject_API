from main_console_app.data_base import all_numbers_cards, history_transactions


def get_avtoriz_data():
    print("Укажите Ваш логин и пароль")
    login, password = input(), input()
    while login == "" or password == "":
        print("Укажите Ваш логин и пароль")
        login, password = input(), input()
    return login, password


def add_transaction_to_history(all_tax, from_card, to_card, transfer_summ, status):
    history_transactions.append(
        {"from_card": from_card, "to_card": to_card, "transfer_sum": transfer_summ, "tax": all_tax,
         "status": status})


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

