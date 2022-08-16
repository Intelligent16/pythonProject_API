


def get_avtoriz_data():
    print("Укажите Ваш логин и пароль")
    login, password = input(), input()
    while login == "" or password == "":
        print("Укажите Ваш логин и пароль")
        login, password = input(), input()

    return login, password



