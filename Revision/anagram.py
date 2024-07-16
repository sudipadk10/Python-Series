# wap to check if two string are anagram (contain same charecter in different order or not 

first = input("ENter first string :")
second = input("Enter second string :")

if len(first)!=len(second):
    print("Not anagram!!")
else:
    l=len(first)
    for i in range(l):
        if(first[i]!=second[l-i-1]):
            break
       
    if i!= l-1:
        print("Not anagram")
    else:
        print("anagram")