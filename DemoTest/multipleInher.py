class opeartionDemo:

    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "({0}, {1})".format(self.a, self.b)

    def __add__(self, other):
        x = self.a + other.a
        # y = self.b + other.b
        return opeartionDemo(x)

    def addingNum(self, c, d):
        sum = c + d
        return sum


open = opeartionDemo(2, 5)
print(open)
sumValue = open.addingNum(1, 6)
print(sumValue)


