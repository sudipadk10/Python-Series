item = {
    'Pizza' : 300,
    'Burger': 250,
    'Fries' : 150,
    'Cola'  : 50,
    'Pasta' : 400
}

print("Welcome to the Food Ordering System!")
print("Current Menu:")
for item_name, price in item.items():
    print(f"{item_name}:\t${price}")

order= {}
print("(Note : Enter blank if you are done .)")
while True :
    key = input("Enter item :")
    if key == '':
        break
    value = int(input("Enter quantity :"))
    order[key] = value

total = 0

for i in order.keys():
    total += item[i] * order[i]

print("--------Your Bill---------")
print()
for i in order.keys():
    print(f"{i} : {order[i]} x ${item[i]} = ${item[i] * order[i]}")
print("--------------------------")
print(f"Total  :\t${total}")
Discount = 0.1*total
vat = (total- Discount)*0.13
Final_total = total - Discount + vat
print(f"Discount :\t${Discount}")
print(f"Vat :     \t${vat}")
print(f"Final Total :\t${Final_total}")
print("Thank you for your order!")
