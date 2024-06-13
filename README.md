Veterinary Clinic Management System

Overview
The Veterinary Clinic Management System is a command-line application built in Python for managing the operations of a veterinary clinic. It allows veterinarians and staff to efficiently handle pets, owners, appointments, treatments, and medical records within a clinic database. The application uses SQLite for data storage and integrates with a CLI for interactive use.

Features
Database Management: Uses SQLite for storing data with tables for pets, owners, veterinarians, appointments, treatments, and medical records.

CRUD Operations: Supports Create, Read, Update, and Delete operations for all main entities through an intuitive command-line interface.

Seed Data: Provides initial data setup through seed scripts to populate the database with sample pets, owners, veterinarians, appointments, treatments, and medical records.

Project Structure
The project follows a structured approach with different modules and scripts organized into directories:

graphql
Copy code
Veterinary-clinic-management-system/
│
├── database/              # Contains database scripts and setup
│   ├── create_tables.sql  # SQL script for creating database tables
│   ├── db_helper.py       # Helper functions for interacting with SQLite
│   ├── setup_db.py        # Script to set up the database
│
├── lib/                   # CLI and debugging scripts
│   ├── cli.py             # Command-line interface for user interaction
│   ├── debug.py           # Script for debugging and database setup
│   ├── helpers.py         # Helper functions (placeholder)
│
├── models/                # Model classes for database entities
│   ├── __init__.py        # Initialization of models package
│   ├── appointment.py     # Appointment model
│   ├── medical_record.py  # Medical record model
│   ├── owner.py           # Owner model
│   ├── pet.py             # Pet model
│   ├── treatment.py       # Treatment model
│   ├── veterinarian.py    # Veterinarian model
│
├── main.py                # Entry point of the application
├── Pipfile                # Dependencies management using Pipenv
├── Pipfile.lock           # Locked dependencies file
└── README.md              # Project overview and instructions

Installation and Setup
Prerequisites
Python: Ensure Python 3.6 or higher is installed.
Pipenv: Use pip to install Pipenv if not already installed:
bash
Copy code
pip install pipenv
Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/Veterinary-clinic-management-system.git
cd Veterinary-clinic-management-system
Install Dependencies:
Copy code
pipenv install

Activate Virtual Environment:
Copy code 
pipenv shell

Setup Database:
Copy code
python3 database/setup_db.py
Usage
Running the Application
CLI Application:

bash
Copy code
python3 lib/cli.py
Debugging and Database Setup:

bash
Copy code
python3 lib/debug.py
SQLite Commands
Access SQLite Shell:

bash
Copy code
sqlite3 vet_clinic.db

View Table Schema:
SQLite

Copy code
.schema table_name

Clear Table Data:
SQLite

Copy code
DELETE FROM table_name;
Sample Data
Adding Sample Data in SQLite Shell:
SQL 
Copy code
INSERT INTO owner (name, email, phone) VALUES
    ('John Doe', 'john@gmail.com', '789675434'),
    ('Jane Smith', 'jane@gmail.com', '9876543210'),
    ('Orlando Sky', 'orlando@gmail.com', '719132133'),
    ('Lucy Smiles', 'lucy@gmail.com', '723633827');

-- Similar inserts for a pet, veterinarian, appointment, treatment, and medical_record tables

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT




