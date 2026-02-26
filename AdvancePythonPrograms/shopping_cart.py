cart = {}

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    if name in cart:
        cart[name]['quantity'] += quantity
    else:
        cart[name] = {"price": price, "quantity": quantity}

def remove_item():
    name = input("Enter item name to remove: ")
    if name in cart:
        del cart[name]

def view_cart():
    total = 0
    for item, details in cart.items():
        item_total = details["price"] * details["quantity"]
        total += item_total
        print(item, "Total:", item_total)
    print("Total Bill:", total)

while True:
    print("\n1.Add 2.Remove 3.View 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        break