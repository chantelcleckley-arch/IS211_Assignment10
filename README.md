
# IS211 Assignment 10

## Week 10: Relational Databases - SQL and SQLite

This assignment explores relational databases using SQL, SQLite, and Python.

## Part I: Music Database

I created a music.sql file containing three tables:

- artist: Stores artist information.
- album: Stores albums and connects each album to an artist.
- song: Stores songs, track numbers, song durations, and their associated albums.

Primary and foreign keys connect the tables.

## Part II: Pets Database

I created a SQLite database called pets.db containing three tables: person, pet, and person_pet.

### load_pets.py
This script inserts four people, six pets, and their ownership relationships into the database.

### query_pets.py
This script allows users to enter a person's ID and view their information and pets. It also handles invalid IDs and continues running until the user enters -1.

## What is the purpose of the person_pet table?

The person_pet table connects people to their pets using their ID numbers. It acts as a link between the person and pet tables, making it possible to see which pets belong to each person without repeating information. This helps keep the database organized.

## Running the Programs

To load the data:

python3 load_pets.py

To search for people and pets:

python3 query_pets.py
