from book_data import load_books

def view_books():
    """Display all books in a user-friendly format."""
    books = load_books()
    if not books:
        print("\nNo books available.")
        return

    print("\n=== List of Books ===")
    for book in books:
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"ISBN: {book['isbn']}")
        print(f"Genre: {book['genre']}")
        print(f"Price: ${book['price']:.2f}")
        print(f"Quantity in stock: {book['quantity']}")
        print("-" * 20)