print("hello world")


def odd(stard,end):
    for i in range(stard, end):
        if i % 2 == 1:
            print(i)


def even(stard,end):
    for i in range(stard, end):
        if i % 2 == 0:
            print(i)


odd(1, 101)
even(1, 101)
