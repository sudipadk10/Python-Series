class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.address = "Biratnagar"
    

class student(person) :
    def __init__(self,name,age,roll,address):
        super().__init__(name,age)
        self.address=address
        self.roll=roll
        
        

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("roll:",self.roll)
        print("address :",self.address)


s = student("Sudip", 19,8,"brt")
s.display()
