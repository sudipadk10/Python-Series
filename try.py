def main():
    yell("This", "is", "Hello")

def yell(*words):
    uppercased = [word.upper() for word in words] #List comprehensions
    print(*uppercased)   #unpack the list

if __name__ =="__main__":
    main()