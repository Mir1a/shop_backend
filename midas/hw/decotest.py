def procent(func):
    def take_procent():
        new_list = func()
        #сумма заказа
        first_arg = new_list[0]
        #скидка
        second_arg = new_list[1]
        result = first_arg - first_arg * (second_arg/100)
        return result
    return take_procent

@procent
def taker_data():
    return [100, 20]

print(taker_data())
