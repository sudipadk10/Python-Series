class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class student(person):
    pass

s = student("Sudip" , 19)
print(s.name)
print(s.age)