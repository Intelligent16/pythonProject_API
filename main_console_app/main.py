

from data_output.console_data_output import avtorization, print_current_user, exit_user, registration, \
    create_card, print_all_card_info, print_all_card_user
from data_input.console_data_input import transfer_to_card


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


# comment
# comment 2

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
    elif comand == 0:
        break



# перевод с карты на карту сделать до концйа без комиссии, сделать итоговый мердж, подтвердить его

#сделать ветку на основе дев по завешению сделать мердж (создать, но не нажимать пулл реквест!!!!!)
# если самому себе, то без комиссии,
# если другому: до 1000 - 50 р
#               1000-10000 - 2%
#               более 10000 - 1%
# список транзакций: с номера на номер, еол-во, статус(успешно, нет)
# СРОЧНАААА!!!!! GitHub





#
# Гит игру 10 не срочно
# SQL 3
# Фастапи 2
# Базовые команды Гита через Пайчарм 1
#
