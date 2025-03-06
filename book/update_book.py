from book_data import load_books, save_books

def update_book():
    """Update book details by ISBN."""
    books = load_books()
    isbn = input("\nEnter ISBN of the book to update: ")
    for book in books:
        if book['isbn'] == isbn:
            print("\nCurrent Details:")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Genre: {book['genre']}")
            print(f"Price: ${book['price']:.2f}")
            print(f"Quantity in stock: {book['quantity']}")

            title = input("Enter new title (leave blank to keep current): ")
            if title:
                book['title'] = title

            author = input("Enter new author (leave blank to keep current): ")
            if author:
                book['author'] = author

            genre = input("Enter new genre (leave blank to keep current): ")
            if genre:
                book['genre'] = genre

            price = input("Enter new price (leave blank to keep current): ")
            if price:
                book['price'] = float(price)

            quantity = input("Enter new quantity (leave blank to keep current): ")
            if quantity:
                book['quantity'] = int(quantity)

            save_books(books)
            print("Book updated successfully.")
            return
    print("Error: Book not found.")