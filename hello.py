def main():
    name = input("What's your name ?")
    print(hello(name))

def hello(x = "World"):
    return f"Hello , {x}"

if __name__ == "__main__":
    main()
    