# x=float(input("What is x ? "))
# y=float(input("What is y ? "))


# z=x/y
# print(f"{z:.2f}")    

# z=round(x+y)
# print(f"{z:,}")    



def main():
    x=int(input("What's x ? "))
    print("x squared is ",square(x))

def square(n):
    return pow(n,2)
main()