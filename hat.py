import random

class Hat:
    houses = [ "Btr" , "Ktm" , "Daran" , "Rtm"]

    @classmethod
    def sort(cls, name ):
        print( name , "is in", random.choice(cls.houses))
              

Hat.sort("Harry")