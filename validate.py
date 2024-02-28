import re

email = input("Enter your email :").strip()

# below : . means any charecter and + means atleast 1 repeatation , ? means 0 or 1 repeatation
#replaced . by [^@] which means all charecters except @
#replace [^@] by \w which indicates all alfanumerics and underscore"_"
if re.search(r"^\w+@(\w+\.)?\w+\.(com|gov|edu|org)$" , email , re.IGNORECASE ):  #r = raw string , '\.' literally indicates "." , ^ and $ indicates start and end
    print("Valid") 
else:
    print("Invalid")
