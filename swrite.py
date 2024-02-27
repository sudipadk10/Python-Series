import csv

name = input("Enter your name :")
home = input("Enter your home :")

with open("students.csv" , "a") as file:
    writer =csv.DictWriter(file , fieldnames=["name" , "home"])
    writer.writerow({"name":name , "home": home})
    