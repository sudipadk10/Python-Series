def main():
    n = int(input("Enter a number :"))
    for s in range(n):
        print(*emoji(s))

def emoji(n):
    butts = []
    for i in range(n):
        butts.append("🦋"*i)
    return butts
if __name__ == "__main__":
    main()