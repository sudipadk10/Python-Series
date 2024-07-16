#Guess the number in times 
import random
def main():
    number = random.choice(range(10))
    print("Welcome to the Guess the Number Game!")

    guess = int(input("Guess a number between 0 and 9 :"))
    count = 1
    while True:
        if guess > number:
            print("The number is smaller than this .")
        elif guess < number:
            print("The number is larger than this .")
        else:
            print("Congratulations! You guessed the correct number.")
            print(f'You took {count} guesses.')
            break
        guess = int(input("Guess again : "))
        count += 1

if __name__ == "__main__":
    main()

