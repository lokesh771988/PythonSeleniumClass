def find_sq(num):
    result = num * num
    return result


abc = lambda number: print("Hello abc", find_sq(number))


abc(5)


abc1 = lambda a, b: print("Hello ", (a + b))


abc1(5, 9)