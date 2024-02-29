import re
url = input("Enter your twitter url :").strip()
#(?: ) is non capturing which doesn't count in group
if matches := re.search(r"^(?:https?://)?(?:www.)?twitter\.com/([\w+)" , url , re.IGNORECASE ):
    print(f"Username : {matches.group(1)}")