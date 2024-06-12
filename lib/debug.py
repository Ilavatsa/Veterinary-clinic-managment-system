from models.pet import Pet
from models.appointment import Appointment
from models.owner import Owner
from models.veterinarian import Veterinarian
from models.treatment import Treatment
from datetime import datetime

import ipdb

def reset_database():
    # Initialize model instances
    pet = Pet()
    appointment = Appointment()
    owner = Owner()
    veterinarian = Veterinarian()
    treatment = Treatment()
    
    # Drop existing tables
    pet.drop_table()
    appointment.drop_table()
    owner.drop_table()
    veterinarian.drop_table()
    treatment.drop_table()

    # Create new tables
    pet.create_table()
    appointment.create_table()
    owner.create_table()
    veterinarian.create_table()
    treatment.create_table()

    # Create seed data for pets
    pet.create("Bella", "Dog", "Labrador", 3, 1)
    pet.create("Max", "Cat", "Siamese", 2, 2)
    # Add more seed data for pets if needed

    # Create seed data for appointments
    appointment.create(1, datetime.now(), 'scheduled', 'Routine checkup')
    appointment.create(2, datetime.now(), 'completed', 'Vaccination')
    # Add more seed data for appointments if needed

    # Create seed data for owners
    owner.create("John Doe", "john@gmail.com", "789675434")
    owner.create("Jane Smith", "jane@gmail.com", "9876543210")
    # Add more seed data for owners if needed

    # Create seed data for veterinarians
    veterinarian.create("Dr. Felicity Muhonja Ilavatsa", "Surgery", "123456789")
    veterinarian.create("Dr. John Waweru", "Dentistry", "987654321")
    # Add more seed data for veterinarians if needed

    # Create seed data for treatments
    treatment.create(1, 1, datetime.now(), "Vaccination")
    treatment.create(2, 2, datetime.now(), "Dental cleaning")
    # Add more seed data for treatments if needed

# Reset the database and start debugging session
reset_database()
ipdb.set_trace()


