class a:

    def pratent(self):
        print("diplay parent")

class b:

    def deisplay(self):
        print("parent 2")

class c(a, b):

    def deisplay(self):
        print("child")


c1 = c()
c1.deisplay()
c1.pratent()