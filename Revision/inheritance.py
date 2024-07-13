class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("hi")
    

class student(person) :
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.name=name
        self.age=age
        self.roll=roll
        

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("roll:",self.roll)


s = student("Sudip", 19,8)
s.display()
