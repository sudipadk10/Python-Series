
class Student : #creating class
    def __init__(self, name , house):      #Creating constructor with temp object self getting two parameters name and house.
        self.name = name   #calling setter from here
        self.house =house
        
    def __str__(self):
        return f"{self.name} is from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid Name")
        self._name=name

    @property
    def house(self):
        return self._house  # _house is instance variable which can't call setter

    @house.setter
    def house(self, house):
        if house not in ["Biratnagar" , " Itahari" , "Kathmandu" , "Ratuwamai"]:
                raise ValueError("Invalid house")
        self._house = house 

def main():
    student = get_student()
    # student._house ="Hounted house"    # The _ denotes instance variable which won't call setter.
    print(student)

def get_student():
    name = input("Name :")
    house = input("House :")
    student= Student(name , house)  # Creating object and calling constructor.
    return student

if __name__ == "__main__" :
    main() 

