menu = {
    "pizza": 40,
    "pasta":100,
    "burger":60,
    "salad":70,
    "coffee":80
}
#print(menu)
print("Welcome to our restaurant! Here's the menu:")
for item, price in menu.items():
    print(f"{item.title()}: Rs {price}")
#print("Pizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffe :Rs 80")

order_total = 0
order_summary={}
button=""
items= input("Enter the name of items with quantity you want to order comma separated\n").split(",")



#if item1.split(",") in menu:
for item in items:
    item = item.strip().lower()
    if item in menu:
        order_total = order_total + menu[item]
        order_summary[item]=menu[item]
    # print(item)
        #print(f"Your item {item.title()} has been added to your order list")

    else:
        print(f"Ordered item {item.title()} is not available yet")
#print(order_summary)

while True:
    another_order = input("Do you want to add another item? (Yes/No)\n")
    if another_order.lower() == "yes":
        item2 =input("Enter the name of the second item = ")
        if item2 in menu:
            order_total = order_total+menu[item2]
            order_summary[item2]=menu[item2]
            print(f"Item {item2} has been added to order list")
        else:
            print(f"Ordered item {item2} is not available.")
    else:
        break
print("---- Bill Summary ----")
for item,price in order_summary.items():
    print(f"{item.title():<15} = Rs {price}")
print(f"{'Total Amount':<15} = Rs {order_total}")
