from midas.models import User
from django.db.models import F

# 1. Создать пользователя
# 2. Создать продукт(Item)
# 3. Создать заказ(Order) с пользователем и продуктом, которые у создали
# В этой функции верни Order.id(вернуть айдишник нового заказа)
def task1():
    return None


# 1.Получить всех пользователей у которых есть заказы
# 2.Отпимизировать запрос(В запросе должны быть поля: email, id, список заказов)
def task2():
    return None

# Сделать несколько заказов с разным количеством товаров
# 1. Через annotate подсчитать сумму предметов в заказах
# 2. Через update изменить значениe поля sum_price у заказа (используй F)
def task3():
    return None


def main():
    print(task1())
    print(task2())
    print(task3())
