menu =  {
    'Pizza':50,
    'Burger':70,
    'Salad':30, 
    'Coffee':80,
    }

print("Welcome to Python Resturant")
print(" Pizza:50\n Burger:70\n Salad:30\n Coffee:80 ")

order_total = 0

item_1 = input("Enter the item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item ? (yes/No)")
if another_order == "Yes": 
    item_2 = input("Enter the name of the second item = ")
if item_2 in menu :
        order_total += menu[item_2]
        print(f"item {item_2} has been added to your order")
else:
    print(f"ordered item {item_2} is not available !")

print(f"The total amount of items to pay is {order_total}")
        
