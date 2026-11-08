
import sqlite3

# Connect to the database
conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

while True:
    person_id = input("Enter a person's ID (-1 to quit): ")

    # Exit when the user enters -1
    if person_id == "-1":
        print("Goodbye!")
        break

    # Check for a valid ID number
    try:
        person_id = int(person_id)
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Find the person
    cursor.execute(
        "SELECT * FROM person WHERE id = ?",
        (person_id,)
    )

    person = cursor.fetchone()

    if person is None:
        print("Person not found.")
        continue

    # Display the person's information
    first_name = person[1]
    last_name = person[2]
    age = person[3]

    print(f"\n{first_name} {last_name}, {age} years old")

    # Find all pets belonging to this person
    cursor.execute(
        """
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
        """,
        (person_id,)
    )

    pets = cursor.fetchall()

    if not pets:
        print("This person has no pets.")
    else:
        for name, breed, pet_age, dead in pets:
            status = "deceased" if dead == 1 else "alive"

            print(
                f"{first_name} {last_name} owned "
                f"{name}, a {breed}, that was "
                f"{pet_age} years old ({status})."
            )

    print()

# Close the database
conn.close()
