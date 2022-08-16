from Fast_API.main import app


@app.post("/num_and_meth/{num1}, {num2}, {meth}")
async def num_and_meth(num1: int, num2: int, meth: str):

    if meth == "+":
        return {"message": num1 + num2}
    elif meth == "-":
        return {"message": num1 - num2}
    elif meth == "*":
        return {"message": num1 * num2}
    elif meth == "/":
        return {"message": num1 / num2}

        # Принимаетсся два числа и 1 метод
        # Принимается операция (+ - х / )
        # Получить результат

        # Консоль
        # авториз/регист пользователя
        # авторизированный может:
        # создать кошелек
        # отредактировать имя кошелька
        # перевести с одного кош на другой кош
        # ИД кошелька генерировать при момощи GUID
        # можно посмотреть список кошельков и имя пользователя
        # неавторизированный:
        # только регистрация
        #
