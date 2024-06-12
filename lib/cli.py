import sys

def display_menu():
    print("Veterinary Clinic Management System")
    print("1. Add Pet")
    print("2. Add Owner")
    print("3. Add Veterinarian")
    print("4. Add Appointment")
    print("5. Add Treatment")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_pet()
        elif choice == '2':
            add_owner()
        elif choice == '3':
            add_veterinarian()
        elif choice == '4':
            add_appointment()
        elif choice == '5':
            add_treatment()
        elif choice == '6':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def add_pet():
    # Add pet logic here
    pass

def add_owner():
    # Add owner logic here
    pass

def add_veterinarian():
    # Add veterinarian logic here
    pass

def add_appointment():
    # Add appointment logic here
    pass

def add_treatment():
    # Add treatment logic here
    pass

if __name__ == "__main__":
    main()


