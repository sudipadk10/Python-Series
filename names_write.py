name= input("What's your name ? ")

#using with it will automatically open and close the file
with open("names.txt" , "a") as file:         
    file.write(f"{name}\n")
    