class addition:

    def sum_my(self, a, b):
        sum = a + b
        print("my sum value ", sum)


class child(addition):
    pass


math = child()
math.sum_my(2, 3)
