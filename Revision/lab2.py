def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def main():
    while(True):
            print("The operations are :\n1. Addition \n2. Subtraction \n 3.Multiplication \n4.Division\n5.Quit ")
            choice = int(input("Enter your choice :"))
            
            if choice == 5:
                break
            elif choice > 5:
                print("Invalid choice. Please try again.")
                continue
            else:
                a = float(input("Enter first number : "))
                b = float(input("Enter second number : "))
                try:
                    if choice == 1:
                        print(add(a,b))
                    elif choice == 2:
                        print(sub(a,b))
                    elif choice == 3:
                        print(mul(a,b))
                    elif choice == 4:
                        print(div(a,b))
                except:
                    print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()