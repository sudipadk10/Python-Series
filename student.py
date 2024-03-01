def main():
    student=student_data()
    print(f"{student[0]} is from {student[1]}")

def student_data():
    return (input("Name :"), input("House :"))  #returning a tuple indicated by () . Its value can not be changed.
                                                #IF there was [] then it is list which value can be changed.
if __name__ == "__main__":
    main()
    