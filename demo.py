print("Hello")


## i am adding a  new class

class a:
    def __init__(self):
        self.b=10
        print("initialized class a")
    def fn(self):
        self.b = self.b +10
        print("b=",self.b)

apple=a()
apple.fn()


