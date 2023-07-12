
menu = []


def add_dish():
    dish_id = input("Enter dish ID: ")
    dish_name = input("Enter dish name: ")
    price = input("Enter price: ")
    availability = input("Is this available? (yes/no): ")


    dish = {
    "dish_id":dish_id,
    "dish_name":dish_name,
    "price": price,
    "availability": availability.lower() == "yes"
    }

    menu.append(dish)
    print("dish added to the menu.")


def remove_dish():
    dish_id = input("Enter the dish ID to remove: ")

    for dish in menu:
        if dish["dish_id"] == dish_id:
            menu.remove(dish)
            print("Dish removed from the menu")
            return

    print("Dish not found in the menu.")




def update_availability():
    dish_id= input("Enter the dish ID to update: ")

    for dish in menu:
        if dish["dish_id"] == dish_id:
           new_availability = input("Enter new availability (yes/no): ")
           dish["availability"] = new_availability.lower() == "yes"
           print("Availability updated")
           return
    
    print("Dish not found in the menu")



def display_menu():
    print("Menu:")
    for dish in menu:
        print(f"ID: {dish['dish_id']}, Name: {dish['dish_name']}, Price: {dish['price']}, Availability: {dish['availability']}")



while True:
    print("\nZesty Zomato Menu Management System")
    print("1. Add a new dish")
    print("2. Remove a dish")
    print("3. Update dish availability")
    print("4. Display menu")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")  


    if choice == "1":
        add_dish()
    elif choice == "2":
        remove_dish()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        display_menu()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
