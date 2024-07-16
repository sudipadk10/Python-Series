
class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)

class student(person):
    def __init__(self,name,rollno):
        self.name = name
        self.rollno =rollno

    def display(self):
        print(self.name,self.rollno)


class teacher(person):
    def __init__(self , tid ,name ):
        self.tid = tid
        self.name = name

    def display(self):
        print(self.tid,self.name)



s = student("student",1)
t = teacher("teacher",2)


for x in [s,t]:
    x.display()
    