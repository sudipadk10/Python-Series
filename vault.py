class vault:
    def __init__(self, jem , diamond , gold):
        self.jem = jem
        self.diamond = diamond
        self.gold = gold

    def __str__(self):
        return f"{self.jem} jems , {self.diamond} diamonds , {self.gold} golds"
    def __add__(self,other):
        jem = self.jem + other.jem
        diamond = self.diamond + other.diamond
        gold = self.gold + other.gold
        return vault(jem , diamond , gold)


harry = vault(100,50,25)
carry = vault(50,35,75)
total = harry + carry   #operator overloading
print(total)