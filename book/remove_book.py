from book_data import load_books, save_books

def remove_book():
    """Remove a book by its ISBN."""
    books = load_books()
    isbn = input("\nEnter ISBN of the book to remove: ")
    for book in books:
        if book['isbn'] == isbn:
            books.remove(book)
            save_books(books)
            print("Book removed successfully.")
            return
    print("Error: Book not found.")