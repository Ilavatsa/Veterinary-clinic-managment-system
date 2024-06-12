# cli.py

from models.owner import Owner
from models.pet import Pet
from models.veterinarian import Veterinarian
from models.appointment import Appointment
from models.treatment import Treatment
from models.medical_record import MedicalRecord

def display_menu():
    """Display the menu options."""
    print("\nVeterinary Clinic Management System")
    print("1. Add new owner")
    print("2. View all owners")
    print("3. Delete an owner")
    print("4. Add new pet")
    print("5. View all pets")
    print("6. Delete a pet")
    print("7. Add new veterinarian")
    print("8. View all veterinarians")
    print("9. Delete a veterinarian")
    print("10. Add new appointment")
    print("11. View all appointments")
    print("12. Delete an appointment")
    print("13. Add new treatment")
    print("14. View all treatments")
    print("15. Delete a treatment")
    print("16. Add new medical record")
    print("17. View all medical records")
    print("18. Delete a medical record")
    print("19. Exit")

def add_owner():
    """Function to add a new owner."""
    name = input("Enter owner's name: ")
    address = input("Enter owner's address: ")
    phone_number = input("Enter owner's phone number: ")
    owner = Owner(name, address, phone_number)
    owner.save()
    print("Owner added successfully.")

def view_owners():
    """Function to view all owners."""
    owners = Owner.get_all()
    for o in owners:
        print(o)

def delete_owner():
    """Function to delete an owner."""
    owner_id = int(input("Enter owner ID to delete: "))
    owner = Owner.find_by_id(owner_id)
    if owner:
        owner.delete()
        print("Owner deleted successfully.")
    else:
        print("Owner not found.")

def add_pet():
    """Function to add a new pet."""
    name = input("Enter pet's name: ")
    species = input("Enter pet's species: ")
    breed = input("Enter pet's breed: ")
    age = int(input("Enter pet's age: "))
    owner_id = int(input("Enter owner's ID: "))
    pet = Pet(name, species, breed, age, owner_id)
    pet.save()
    print("Pet added successfully.")

def view_pets():
    """Function to view all pets."""
    pets = Pet.get_all()
    for p in pets:
        print(p)

def delete_pet():
    """Function to delete a pet."""
    pet_id = int(input("Enter pet ID to delete: "))
    pet = Pet.find_by_id(pet_id)
    if pet:
        pet.delete()
        print("Pet deleted successfully.")
    else:
        print("Pet not found.")

def add_veterinarian():
    """Function to add a new veterinarian."""
    name = input("Enter veterinarian's name: ")
    specialty = input("Enter veterinarian's specialty: ")
    veterinarian = Veterinarian(name, specialty)
    veterinarian.save()
    print("Veterinarian added successfully.")

def view_veterinarians():
    """Function to view all veterinarians."""
    veterinarians = Veterinarian.get_all()
    for v in veterinarians:
        print(v)

def delete_veterinarian():
    """Function to delete a veterinarian."""
    veterinarian_id = int(input("Enter veterinarian ID to delete: "))
    veterinarian = Veterinarian.find_by_id(veterinarian_id)
    if veterinarian:
        veterinarian.delete()
        print("Veterinarian deleted successfully.")
    else:
        print("Veterinarian not found.")

def add_appointment():
    """Function to add a new appointment."""
    date = input("Enter appointment date: ")
    reason = input("Enter appointment reason: ")
    pet_id = int(input("Enter pet ID: "))
    veterinarian_id = int(input("Enter veterinarian ID: "))
    appointment = Appointment(date, reason, pet_id, veterinarian_id)
    appointment.save()
    print("Appointment added successfully.")

def view_appointments():
    """Function to view all appointments."""
    appointments = Appointment.get_all()
    for a in appointments:
        print(a)

def delete_appointment():
    """Function to delete an appointment."""
    appointment_id = int(input("Enter appointment ID to delete: "))
    appointment = Appointment.find_by_id(appointment_id)
    if appointment:
        appointment.delete()
        print("Appointment deleted successfully.")
    else:
        print("Appointment not found.")

def add_treatment():
    """Function to add a new treatment."""
    name = input("Enter treatment name: ")
    description = input("Enter treatment description: ")
    cost = float(input("Enter treatment cost: "))
    treatment = Treatment(name, description, cost)
    treatment.save()
    print("Treatment added successfully.")

def view_treatments():
    """Function to view all treatments."""
    treatments = Treatment.get_all()
    for t in treatments:
        print(t)

def delete_treatment():
    """Function to delete a treatment."""
    treatment_id = int(input("Enter treatment ID to delete: "))
    treatment = Treatment.find_by_id(treatment_id)
    if treatment:
        treatment.delete()
        print("Treatment deleted successfully.")
    else:
        print("Treatment not found.")

def add_medical_record():
    """Function to add a new medical record."""
    record_date = input("Enter record date: ")
    details = input("Enter record details: ")
    pet_id = int(input("Enter pet ID: "))
    medical_record = MedicalRecord(record_date, details, pet_id)
    medical_record.save()
    print("Medical record added successfully.")

def view_medical_records():
    """Function to view all medical records."""
    medical_records = MedicalRecord.get_all()
    for mr in medical_records:
        print(mr)

def delete_medical_record():
    """Function to delete a medical record."""
    medical_record_id = int(input("Enter medical record ID to delete: "))
    medical_record = MedicalRecord.find_by_id(medical_record_id)
    if medical_record:
        medical_record.delete()
        print("Medical record deleted successfully.")
    else:
        print("Medical record not found.")

def cli():
    """Main function to run the CLI."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_owner()
        elif choice == '2':
            view_owners()
        elif choice == '3':
            delete_owner()
        elif choice == '4':
            add_pet()
        elif choice == '5':
            view_pets()
        elif choice == '6':
            delete_pet()
        elif choice == '7':
            add_veterinarian()
        elif choice == '8':
            view_veterinarians()
        elif choice == '9':
            delete_veterinarian()
        elif choice == '10':
            add_appointment()
        elif choice == '11':
            view_appointments()
        elif choice == '12':
            delete_appointment()
        elif choice == '13':
            add_treatment()
        elif choice == '14':
            view_treatments()
        elif choice == '15':
            delete_treatment()
        elif choice == '16':
            add_medical_record()
        elif choice == '17':
            view_medical_records()
        elif choice == '18':
            delete_medical_record()
        elif choice == '19':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    cli()
