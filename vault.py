class vault:
    def __init__(self, jem , diamond , gold):
        self.jem = jem
        self.diamond = diamond
        self.gold = gold

    def __str__(self):
        return f"{self.jem} jems , {self.diamond} diamonds , {self.gold} golds"
    

harry = vault(100,50,25)
print(harry)