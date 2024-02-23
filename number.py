def main():
    number=get_int("Enter a number :")
    print(f"The number is {number}")


def get_int(prompt):
    while True :
        try:
            return int(input(prompt))
    
        except ValueError:
            pass

    
main()
