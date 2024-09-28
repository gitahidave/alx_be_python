def display_menu():
    """
    Display the menu options to the user.
    """
    print("\nShopping List Manager")
    print("---------------------")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

def add_item(shopping_list):
    """
    Add an item to the shopping list.
    
    Parameters:
    shopping_list (list): The current shopping list.
    """
    item = input("Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to the list.")

def remove_item(shopping_list):
    """
    Remove an item from the shopping list.
    
    Parameters:
    shopping_list (list): The current shopping list.
    """
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def view_list(shopping_list):
    """
    Display the current shopping list.
    
    Parameters:
    shopping_list (list): The current shopping list.
    """
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("\nCurrent Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

def main():
    shopping_list = []
    while True:
        display_menu()
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
