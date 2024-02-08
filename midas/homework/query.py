import random
from midas.models import User
from product.models import Item
from product.models import Order
from django.db.models import F, Count, Sum, OuterRef, Subquery

# 1. Создать пользователя
# 2. Создать продукт(Item)
# 3. Создать заказ(Order) с пользователем и продуктом, которые у создали
# В этой функции верни Order.id(вернуть айдишник нового заказа)

def task1():
    axe, created = User.objects.get_or_create(name="Axe",
                              last_name="Attacks",
                              born="2022-01-01",
                              is_staff=False,
                              is_active=True,
                              password="pass1",
                              email="axe" + str(random.uniform(1, 99999)) + "@gmail.com")

    result_items = []
    for index in range(5):
        result_items.append(Item(title="Vanguard",
        description="heavy",
        code=random.uniform(1, 99999),
        price=random.randint(1, 1000),
        color="Grey",
        weight="20",
        height="2",
        width="1"))

    items = Item.objects.bulk_create(result_items)

    zakaz_1 = (sum_price=1700,
                                   amount_items=1,
                                   status=True,
                                   user=axe,)
    zakaz_1.items.set(items)
    #zakaz_1.items.add([vanguard])

    return axe, items, zakaz_1
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

    Order.objects\
        .update(amount_items=\
            Subquery(Item.objects\
              .filter(orders__id=OuterRef('id'))\
              .annotate(items_count=Count('id'))\
              .values('items_count')[:1]),
                sum_price=\
            Subquery(Item.objects\
              .filter(orders__id=OuterRef('id'))\
              .annotate(items_sum=Count('price'))\
              .values('items_sum')[:1]),

        )


    # oreders = Order.objects\
    #     .annotate(items_count=Count("items"))\
    #     .update(amount_items=F("items_count"))
    return Order.objects.values("amount_items")


def main():
   task1()
#    print(task2())
#     print(task3())
