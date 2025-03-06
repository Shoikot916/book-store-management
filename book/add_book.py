from book_data import load_books, save_books

def add_book():
    """Add a new book to the store."""
    books = load_books()
    print("\n=== Add a New Book ===")
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    genre = input("Enter genre: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    # Check for duplicate ISBN
    for book in books:
        if book['isbn'] == isbn:
            print("Error: A book with this ISBN already exists.")
            return

    # Add the new book
    books.append({
        'title': title,
        'author': author,
        'isbn': isbn,
        'genre': genre,
        'price': price,
        'quantity': quantity
    })
    save_books(books)
    print("Book added successfully!")