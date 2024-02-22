name=input("What's your name ?  ")

match name:
    case "Ram" | "Shyam" | "Sita" | "Gita" :
        print("Section A")
    case "Radha" | "Krishna" | "Siva" | "Parwati" :
        print("Section B")
    case _:
        print("Who is this ?")
    