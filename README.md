# 📚 Personal Library Manager

A simple Python command-line program that helps you manage your personal book collection. You can add, remove, search, and view books, along with statistics about your reading progress.

---

## 🎯 Features

- Add a new book with details (Title, Author, Year, Genre, Read Status)
- Remove a book by its title
- Search for books by title or author
- View all books in your library
- See statistics:
  - Total number of books
  - Percentage of books read
- Easy-to-use menu system

---

## 💡 How It Works

The program uses a list of dictionaries to store your books. Each dictionary contains:

```python
{
    "title": "Book Title",
    "author": "Author Name",
    "year": 2023,
    "genre": "Genre",
    "read": True  # or False
}
# Personal-Library-Manager
