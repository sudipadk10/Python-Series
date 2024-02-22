
def main():
    x = int( input("what is X ?"))
    if is_even(x):
        print("Even")
    else:
       print("Odd")

def is_even(a):
   return a%2==0

main()