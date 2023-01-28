# OOP
class abc:
    name = ""
    number = 10

    def disply(self):
        print("my function")


obj = abc()
print(obj.number)
obj.name = "Testing"
obj.number = 20
print(obj.name)
print(obj.number)
obj.disply()