import json
import os

DATA_FILE = 'books.json'

def load_books():
    """Load books from the JSON file. If the file doesn't exist, return an empty list."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_books(books):
    """Save the list of books to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(books, file, indent=4)