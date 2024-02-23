def main():
    number=get_int()
    print(f"The number is {number}")


def get_int():
    while True :
        try:
            return int(input("Enter a number :"))
    
        except ValueError:
            pass

    
main()
