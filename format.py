import re
name = input("Enter your name :").strip()   # last,first ``
  #paranthesis forms groups , := is walrus operator used for "if and only if" 
if matches := re.search("^(.+), *(.+)$" , name):  # * indicates 0 or more repeatatioin of whitespace.
   name = matches.group(2) + " " + matches.group(1)

print(f"Hello {name}")