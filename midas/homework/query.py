import random
from midas.models import User
from product.models import Item
from product.models import Order
from django.db.models import F
from django.db.models import Count
from django.db.models import Sum

# 1. Создать пользователя
# 2. Создать продукт(Item)
# 3. Создать заказ(Order) с пользователем и продуктом, которые у создали
# В этой функции верни Order.id(вернуть айдишник нового заказа)

# def task1():
#     axe = User.objects.create(name="Axe",
#                               last_name= "Attacks",
#                               born="2022-01-01",
#                               is_staff=False,
#                               is_active=True,
#                               password="pass1",
#                               email="axe" + str(random.uniform(1, 99999)) + "@gmail.com")
#     vanguard = Item.objects.create(title="Vanguard",
#         description="heavy",
#         code=random.uniform(1, 99999),
#         price=1700,
#         color="Grey",
#         weight="20",
#         height="2",
#         width="1"
#     )
#     zakaz_1 = Order.objects.create(sum_price=1700,
#                                    amount_items=1,
#                                    status=True,
#                                    user=axe,)
#     zakaz_1.items.set([vanguard])
#     #zakaz_1.items.add([vanguard])

#     return axe, vanguard, zakaz_1
# #Из-за того, что повторял по кд пока делал высвечивало, что код и почта уже заняты, поэтому добавил рандом
# #понятно, что можно и без него
#
#
# 1.Получить всех пользователей у которых есть заказы
# 2.Отпимизировать запрос(В запросе должны быть поля: email, id, список заказов)
# #def task2():
#     # users_with_orders = User.objects.select_related("order").filter(order__isnull=False).distinct().only("email", "id", "order")
#     # return users_with_orders

# Сделать несколько заказов с разным количеством товаров
# 1. Через annotate подсчитать сумму предметов в заказах
# 2. Через update изменить значениe поля sum_price у заказа (используй F)
def task3():
    oreders = Order.objects\
        .annotate(items_count=Count("items"))\
        .update(amount_items=F("items_count"))
    return oreders


def main():
#    print(task1())
#    print(task2())
    print(task3())
