class myclass :
    def __iter__(self):
        self.x=1
        return self

    def __next__(self):
        a=self.x
        self.x+=1
        return a
    
obj = myclass()
myiter = iter(obj)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))