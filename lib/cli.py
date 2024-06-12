from lib.helpers import get_valid_int, get_non_empty_string, get_choice
from lib.debug import log_info, log_error
from models.pet import Pet

def display_menu():
    """Display the menu options."""
    print("Veterinary Clinic Management System")
    print("1. Add new pet")
    print("2. View pet information")
    print("3. Update pet information")
    print("4. Delete pet")
    print("5. Exit")

def add_pet():
    """Function to add a new pet."""
    try:
        print("Adding new pet...")
        name = get_non_empty_string("Enter pet's name: ")
        age = get_valid_int("Enter pet's age: ", min_val=0)
        type = get_non_empty_string("Enter pet's type (e.g., Dog, Cat): ")
        owner_id = get_valid_int("Enter owner's ID: ", min_val=1)
        
        pet = Pet.create(name=name, age=age, type=type, owner_id=owner_id)
        log_info(f"Added new pet: {pet}")
        print("Pet added successfully.")
    except Exception as e:
        log_error(f"Error adding pet: {e}")
        print("Failed to add pet. Please try again.")

def view_pet():
    """Function to view pet information."""
    print("Viewing pet information...")
    # Add code to handle viewing pet information

def update_pet():
    """Function to update pet information."""
    print("Updating pet information...")
    # Add code to handle updating pet information

def delete_pet():
    """Function to delete a pet."""
    print("Deleting pet...")
    # Add code to handle deleting a pet

def cli():
    """Main function to run the CLI."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_pet()
        elif choice == '2':
            view_pet()
        elif choice == '3':
            update_pet()
        elif choice == '4':
            delete_pet()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    cli()

