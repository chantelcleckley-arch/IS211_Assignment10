
import sqlite3

# Connect to the existing database
conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

# Add people
people = [
    (1, "James", "Smith", 41),
    (2, "Diana", "Greene", 23),
    (3, "Sara", "White", 27),
    (4, "William", "Gibson", 23)
]

# Add pets
pets = [
    (1, "Rusty", "Dalmation", 4, 1),
    (2, "Bella", "Alaskan Malamute", 3, 0),
    (3, "Max", "Cocker Spaniel", 1, 0),
    (4, "Rocky", "Beagle", 7, 0),
    (5, "Rufus", "Cocker Spaniel", 1, 0),
    (6, "Spot", "Bloodhound", 2, 1)
]

# Connect people to their pets
person_pets = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

# Insert the data
cursor.executemany(
    "INSERT OR REPLACE INTO person VALUES (?, ?, ?, ?)",
    people
)

cursor.executemany(
    "INSERT OR REPLACE INTO pet VALUES (?, ?, ?, ?, ?)",
    pets
)

# Clear existing relationships to avoid duplicates
cursor.execute("DELETE FROM person_pet")

cursor.executemany(
    "INSERT INTO person_pet VALUES (?, ?)",
    person_pets
)

# Save changes and close database
conn.commit()
conn.close()

print("People and pets loaded successfully!")
