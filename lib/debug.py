import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
    pet.create("Charlie", "Dog", "Husky", 3, 3)
    pet.create("Sly", "Cat", "Egyptian Cat", 4, 4)
    

    # Create seed data for appointments
    appointment.create(1, datetime.now(), 'scheduled', 'Routine checkup')
    appointment.create(2, datetime.now(), 'completed', 'Vaccination')
    appointment.create(3, datetime.now(), 'scheduled', 'To be performed')
    appointment.create(4, datetime.now(), 'scheduled', 'Testing')
    


    

    # Create seed data for owners
    owner.create("John Doe", "john@gmail.com", "789675434")
    owner.create("Jane Smith", "jane@gmail.com", "9876543210")
    owner.create("Orlando Sky", "orlando@gmail.com", "719132133")
    owner.create("Lucy Smiles", "lucy@gmail.com", "723633827")
    

    # Create seed data for veterinarians
    veterinarian.create("Dr. Felicity Muhonja Ilavatsa", "Dermatologist", "123456789")
    veterinarian.create("Dr. John Waweru", "Dentist", "987654321")
    veterinarian.create("Dr. Marcelous Griffins", "Surgeon", "987679201")
    veterinarian.create("Dr. Nora Roberts", "Opthamologist", "746028753")
    

    # Create seed data for treatments
    treatment.create(1, 1, datetime.now(), "Skin")
    treatment.create(2, 2, datetime.now(), "Dental cleaning")
    treatment.create(3, 3, datetime.now(), "Vaccination")
    treatment.create(4, 4, datetime.now(), "Eyes")

# Reset the database and start debugging session
reset_database()
ipdb.set_trace()



