class parent:

    name = ""
    def display(self):
        print("my parent class")


class child(parent):

    def display(self):
        super().display()
        print("child class")


child1 = child()
child1.name = "Testing"
child1.display()
print(child1.name)