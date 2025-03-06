from book_data import load_books

def search_books():
    """Search for books by title, author, genre, or ISBN."""
    books = load_books()
    search_term = input("\nEnter search term (title, author, genre, or ISBN): ").lower()
    found_books = [book for book in books if 
                   search_term in book['title'].lower() or 
                   search_term in book['author'].lower() or 
                   search_term in book['genre'].lower() or 
                   search_term == book['isbn']]

    if found_books:
        print("\n=== Search Results ===")
        for book in found_books:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"ISBN: {book['isbn']}")
            print(f"Genre: {book['genre']}")
            print(f"Price: ${book['price']:.2f}")
            print(f"Quantity in stock: {book['quantity']}")
            print("-" * 20)
    else:
        print("No books found matching the search term.")