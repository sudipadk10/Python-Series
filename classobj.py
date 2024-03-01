
class Student : #creating class
    def __init__(self, name , house):      #Creating constructor with temp object self getting two parameters name and house.
        if not name :
            raise ValueError("Invalid Name")   #raises the value error if condition macthes.
        if house not in ["Biratnagar" , " Itahari" , "Kathmandu" , "Ratuwamai"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house =house
        
    def __str__(self):
        return f"{self.name} is from {self.house}"


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name :")
    house = input("House :")
    student= Student(name , house)  # Creating object and calling constructor.
    return student

if __name__ == "__main__" :
    main() 

