def my_generator(massive):

    for i in massive:
        yield i

n_list = "hello world"

def try_1(massive):
    for s in my_generator(massive):
        print(s)
    pass

try_1(n_list)