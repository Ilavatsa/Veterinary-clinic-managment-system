CREATE TABLE IF NOT EXISTS owners (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    phone_number TEXT
);

CREATE TABLE IF NOT EXISTS pets (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT,
    age INTEGER,
    owner_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES owners(id)
);

CREATE TABLE IF NOT EXISTS veterinarians (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    specialty TEXT
);

CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY,
    pet_id INTEGER NOT NULL,
    veterinarian_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    reason TEXT,
    FOREIGN KEY (pet_id) REFERENCES pets(id),
    FOREIGN KEY (veterinarian_id) REFERENCES veterinarians(id)
);

CREATE TABLE IF NOT EXISTS treatments (
    id INTEGER PRIMARY KEY,
    appointment_id INTEGER NOT NULL,
    description TEXT,
    FOREIGN KEY (appointment_id) REFERENCES appointments(id)
);

CREATE TABLE IF NOT EXISTS medical_records (
    id INTEGER PRIMARY KEY,
    pet_id INTEGER NOT NULL,
    description TEXT,
    date TEXT,
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);
