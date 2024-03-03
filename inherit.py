#Incomplete / Just for concept of inheritence
class Wizard:
    def __init__(self,name):
        if not name :
            raise ValueError("Missing Name")
        self.name = name 

class Student(Wizard):       #Inheriting
    def __init__(self,name,house):
        super().__init__(name)
        self.house=house

class Teacher(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
wizard = Wizard("Albus")
student = Student("Harry" , "Gryfindoor")
teacher = Teacher("Proffesser" , "dark arts")

