inventory = {}
FILE_NAME = "inventory.txt"

# Load inventory from file
def load_inventory():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, quantity, price = line.strip().split(",")
                inventory[name] = {
                    "quantity": int(quantity),
                    "price": float(price)
                }
    except FileNotFoundError:
        print("Inventory file not found. Starting with empty inventory.")
    except Exception as e:
        print("Error loading file:", e)

# Save inventory to file
def save_inventory():
    try:
        with open(FILE_NAME, "w") as file:
            for item, details in inventory.items():
                file.write(f"{item},{details['quantity']},{details['price']}\n")
    except Exception as e:
        print("Error saving file:", e)

def add_item():
    try:
        name = input("Enter item name: ").strip()

        if name in inventory:
            print("Item already exists. Use update option instead.")
            return

        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        inventory[name] = {"quantity": quantity, "price": price}
        save_inventory()
        print(f"Item '{name}' added successfully!")

    except ValueError:
        print("Invalid input. Quantity must be integer and price must be number.")

def update_item():
    try:
        name = input("Enter item name to update: ").strip()

        if name not in inventory:
            print("Item not found in inventory.")
            return

        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))

        inventory[name]["quantity"] = quantity
        inventory[name]["price"] = price

        save_inventory()
        print(f"Item '{name}' updated successfully!")

    except ValueError:
        print("Invalid input. Please enter correct numbers.")

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n--- Inventory ---")
    print(f"{'Item':<15}{'Quantity':<10}{'Price':<10}")
    print("-" * 35)

    for item, details in inventory.items():
        print(f"{item:<15}{details['quantity']:<10}{details['price']:<10.2f}")

    print("-" * 35)

def menu():
    load_inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Display Inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()