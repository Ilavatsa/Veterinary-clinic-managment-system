# cli.py

# Define a list to store patient records (each patient represented as a dictionary)
patients = []

def display_menu():
    """Display the menu options."""
    print("Veterinary Clinic Management System")
    print("1. Add new patient with pet")
    print("2. View patient information")
    print("3. Update patient information")
    print("4. Delete patient")
    print("5. Exit")

def add_patient():
    """Function to add a new patient with pet."""
    print("Adding new patient with pet...")
    # Prompt user for patient details
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    # Prompt user for pet details
    pet_name = input("Enter pet's name: ")
    pet_species = input("Enter pet's species: ")
    # Create a new patient record with pet (represented as a dictionary)
    patient = {'name': name, 'age': age, 'pet': {'name': pet_name, 'species': pet_species}}
    # Append the patient record to the list of patients
    patients.append(patient)
    print("Patient with pet added successfully.")

def view_patient():
    """Function to view patient information."""
    print("Viewing patient information...")
    if patients:
        for index, patient in enumerate(patients, start=1):
            print(f"Patient {index}: Name - {patient['name']}, Age - {patient['age']}")
            if 'pet' in patient:
                print(f"    Pet: Name - {patient['pet']['name']}, Species - {patient['pet']['species']}")
    else:
        print("No patients found.")

# Implement update_patient() and delete_patient() similarly

def cli():
    """Main function to run the CLI."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patient()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    cli()
