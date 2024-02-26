
with open("names.txt" , "r") as file:    #we can also do file = open("names.txt" , "r") & we have to close it .
    lines = file.readlines()

for line in lines:                  
    print("Hello " ,line.rstrip())    # .rstrip is equal to end =""

#alternative:

# with open("names.txt" , "r") as file:
#     for line in file:                  
#         print("Hello " ,line , end="")
