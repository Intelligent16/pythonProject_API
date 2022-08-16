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

# {ключ : значение}
# _КЛЮЧ___=======ЗНАЧЕНИЕ==============
# {login: {age: x, password: y}}
#           к____з    к______з
from data_input.console_data_input import get_avtoriz_data
from main_console_app.data_base import users


def check_login(log):
    if log in users:
        return True
    else:
        return False


def check_password(log, pas):
    if users.get(log) is not None and users.get(log) == pas:
        return True
    else:
        return False







# if pas in users["aws"]:
#     pass


# courses = {}
# courses["first"] = "test"
# print(courses)
# x = "part"
# second_cours = {x: 1}
# second_cours["y"] = 3
# courses["second"] = second_cours
# print(courses)
# first_cours = second_cours.copy()
# first_cours[x] = 4
# first_cours["y"] = 5
# courses["first"] = first_cours
# print(courses)
# print("first" in courses)
# print(3 in courses)
# print("part" in courses["first"])
# for key, val in courses.items():
#     print("key", key)
#     print("val", val)
# print("===================")
# for key in courses:
#     print("key", key)
#     print("val", courses[key])
# print("===================")
# print(courses.items())
# print("===================")
# print(courses.keys())
# print(courses.values())
# for key in courses.keys():
#     print(key)
# print("===================")
# a = "mama"
# b = {}
# for i in a:
#     if i not in b:
#         b[i] = i
# print(b.keys())
#
# print("===================")
# a = "mama"
# b = {}
#
# for i in a:
#     if i not in b:
#         b[i] = 1
#     else:
#         b[i] = b[i] + 1
# print(b)
#
# print("В слове", a)
# for key in b:
#     print("Букв", key, b[key], "штук")

# статья
# авторицазия ч-з консоль
# получение данных с консоли в отдельных метод
# словари
#
# ясно нужно спать больше
