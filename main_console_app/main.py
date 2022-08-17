from data_output.console_data_output import avtorization, print_current_user, exit_user, registration, \
    create_card, print_all_card_info, print_all_card_user
from data_input.console_data_input import transfer_to_card, get_history_transactions

def print_all_comands():
    print("Введите номер команды")
    print("1 - авторизация")
    print("2 - регистрация")
    print("3 - текущий пользователь")
    print("4 - выход из системы")
    print("5 - создать карту")
    print("6 - показать список всех карт")
    print("7 - показать список всех карт текущего пользователя")
    print("8 - перевести на другую карту")
    print("9 - получить список транзакций")
    print("0 - завершение программы")

def get_comand():
    while True:
        comand = input()
        if comand.isdigit():
            return int(comand)

while True:
    print_all_comands()
    comand = get_comand()
    if comand == 1:
        avtorization()
    elif comand == 2:
        registration()
    elif comand == 3:
        print_current_user()
    elif comand == 4:
        exit_user()
    elif comand == 5:
        create_card()
    elif comand == 6:
        print_all_card_info()
    elif comand == 7:
        print_all_card_user()
    elif comand == 8:
        transfer_to_card()
    elif comand == 9:
        get_history_transactions()
    elif comand == 0:
        break