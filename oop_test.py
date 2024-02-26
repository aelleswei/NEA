class Parent():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        print(self.a + self.b)
        

class Child(Parent):
    def __init__(self,a,b):
        super().__init__(a,b)
        self.string = 'Hello'
        

child = Child(1,2)
child.add()
print(child.string)