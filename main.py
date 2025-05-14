library = []

def display_menu():
    print("\n📚 Welcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").lower()
    read_status = True if read_input == 'yes' else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }

    library.append(book)
    print("✅ Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found.")

def search_book():
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")

    keyword = input("Enter the search term: ").lower()
    found = False

    for book in library:
        if (choice == '1' and keyword in book["title"].lower()) or \
           (choice == '2' and keyword in book["author"].lower()):
            print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {"Read" if book["read"] else "Unread"}')
            found = True

    if not found:
        print("❌ No matching books found.")

def display_books():
    if not library:
        print("📂 Your library is empty.")
        return

    print("📚 Your Library:")
    for idx, book in enumerate(library, start=1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

def display_stats():
    total = len(library)
    if total == 0:
        print("📊 No books to show statistics.")
        return

    read_count = sum(1 for book in library if book["read"])
    percent = (read_count / total) * 100
    print(f"📈 Total books: {total}")
    print(f"📖 Percentage read: {percent:.1f}%")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            display_books()
        elif choice == '5':
            display_stats()
        elif choice == '6':
            print("📁 Exiting program... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
