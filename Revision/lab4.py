# Create a class student with following properties name, class and adress use People super class with properties age and gender using inheritence link classes.

class people:
    def __init__(self):
        self.age = 19
        self.gender = 'Male'


class student(people):
    def __init__(self):
        super().__init__()
        self.name = 'David'
        self.grade = 9
        self.address ='Biratnagar'

    def display(self):
        print(f"Name : {self.name}")
        print(f"Gender : {self.gender}")
        print(f"Age : {self.age}")
        print(f"Grade : {self.grade}")
        print(f"address : {self.address}")


s = student()
s.display()