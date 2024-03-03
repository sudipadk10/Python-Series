class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance


    def diposit(self,n):
        self._balance += n

    def withdraw(self,n):
        self._balance -= n
        
def main():
    account = Account()
    print("Balance :", account.balance)
    account.diposit(200)
    account.withdraw(50)
    print("Balance :", account.balance)

if __name__ == "__main__":
    main()