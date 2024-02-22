def main():
    number = get()
    meow(number)

def get():
     while True:
        n = int(input("Enter a number :"))
        if n > 0:
            break
     return n  
    



def meow(x):
    for _ in range(x):
        print("Meow")
main()