class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_item(self, name, quantity):
        name_lower = name.lower()
        if name_lower not in self.inventory:
            self.inventory[name_lower] = {'quantity': quantity}
        else:
            self.inventory[name_lower]['quantity'] += quantity

    def remove_item(self, name, quantity):
        name_lower = name.lower()
        if name_lower in self.inventory:
            if self.inventory[name_lower]['quantity'] >= quantity:
                self.inventory[name_lower]['quantity'] -= quantity
                if self.inventory[name_lower]['quantity'] == 0:
                    del self.inventory[name_lower]
                print(f"Removed {quantity} {name}(s) from the inventory.")
            else:
                print("Not enough available.")
        else:
            print("Item not found in the inventory.")

    def check_stock(self, name):
        name_lower = name.lower()
        if name_lower in self.inventory:
            return self.inventory[name_lower]['quantity']
        else:
            return 0

    def update_item(self, name, quantity):
        name_lower = name.lower()
        if name_lower in self.inventory:
            self.inventory[name_lower]['quantity'] = quantity
            print(f"Updated quantity of {name} to {quantity}.")
        else:
            print("Item not found in the inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for name, details in self.inventory.items():
            print(f"Item Name: {name}, Quantity: {details['quantity']}")

    def add_item_from_input(self):
        try:
            name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            self.add_item(name, quantity)
            print(f"Added {quantity} {name}(s) to the inventory.")
        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

    def remove_item_from_input(self):
        try:
            name = input("Enter Item Name to remove: ")
            quantity = int(input("Enter Quantity to remove: "))
            self.remove_item(name, quantity)
        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

    def check_stock_from_input(self):
        name = input("Enter Item Name to check stock: ")
        stock = self.check_stock(name)
        print(f"Stock of {name}: {stock}")


def main():
    warehouse = Warehouse()

    while True:
        print("\nOptions:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Inventory")
        print("4. Check Stock")
        print("5. Update Item Quantity")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            warehouse.add_item_from_input()

        elif choice == '2':
            warehouse.remove_item_from_input()

        elif choice == '3':
            warehouse.display_inventory()

        elif choice == '4':
            warehouse.check_stock_from_input()

        elif choice == '5':
            try:
                name = input("Enter Item Name to update: ")
                quantity = int(input("Enter New Quantity: "))
                warehouse.update_item(name, quantity)
            except ValueError:
                print("Invalid input. Please enter valid numerical values.")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()
