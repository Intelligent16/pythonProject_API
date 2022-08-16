from fastapi import FastAPI
import random

START = "START"
WIN = "WIN"
SMALLER = "SMALLER"
BIGGER = "BIGGER"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


status = START
num = 0


@app.get("/status")
async def check_status():
    global status, num
    if status == START:
        num = random.randint(1, 100)
    elif status == WIN:
        num = random.randint(1, 100)
        status = START
        return {"status": WIN}
    return {"status": status}


@app.post("/send_number/{number}")
async def send_number(number: int):
    global status, num
    if number < 1 or number > 100:
        return {"message": "error, send a number in 1 to 100"}
    elif number > num:
        status = BIGGER
    elif number < num:
        status = SMALLER
    elif number == num:
        status = WIN


num1 = 0
num2 = 0
meth = ''


@app.post("/numbers/{num1}/{num2}")
async def numbers(x: int, y: int):
    global num1, num2
    num1 = x
    num2 = y
    return {"message": [num1, num2]}


@app.post(f"/meth/{meth}")
async def method(operation: str):
    global meth
    meth = operation
    return {"message": meth}


@app.get("/res")
async def res():
    if meth == "+":
        result = num1 + num2
        return {"message": result}
    elif meth == "-":
        result = num1 - num2
        return {"message": result}
    elif meth == "*":
        result = num1 * num2
        return {"message": result}
    elif meth == "/":
        result = num1 / num2
        return {"message": result}

# Принимаетсся два числа
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
