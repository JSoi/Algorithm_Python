mylist = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if mylist[x] != 0:  # 값이 있다면, 그대로 활용
        return mylist[x]
    mylist[x] = fibo(x - 1) + fibo(x - 2)
    return mylist[x]


print(fibo(99))
