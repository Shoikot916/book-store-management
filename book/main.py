from add_book import add_book
from view_book import view_books
from search_book import search_books
from remove_book import remove_book
from update_book import update_book

def main_menu():
    while True:
        print("\n Welcome to Book Store Management System ")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Update Book")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            remove_book()
        elif choice == '5':
            update_book()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()