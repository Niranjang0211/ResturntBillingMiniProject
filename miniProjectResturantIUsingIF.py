menu = {
    "Pizza": 40,
    "Pasta":50,
    "Burger":60,
    "Salad":70,
    "Coffe":80
}
#print(menu)
print("Welcome to our new restaurant and here it is the menu...")
print("Pizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffe :Rs 80")

order_total = 0
item1= input("Enter the name of item you want to order\n").title()
if item1 in menu:
    order_total = order_total+menu[item1]
    print(f"Your item {item1} has been added to your order list")

else:
    print(f"Ordered item {item1} is not available yet")
another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item2 =input("Enter the name of the second item = ")
    if item2 in menu:
        order_total = order_total+menu[item2]
        print(f"Item {item2} has been added to order list")
    else:
        print(f"Ordered item {item2} is not available.")

print(f"The total amount of items to pay is {order_total}")
