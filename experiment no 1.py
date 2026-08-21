
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add a new book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    # Register a new patron
    def register_patron(self, patron):
        self.patrons.append(patron)
        print("Patron registered successfully.")

    # Borrow a book
    def borrow_book(self, book_id, patron_id):
        book = None
        patron = None

        # Find book
        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        # Find patron
        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        if book is None:
            print("Book not found.")
        elif patron is None:
            print("Patron not found.")
        elif book.is_borrowed:
            print("Book is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            print("Book borrowed successfully.")

    # Return a book
    def return_book(self, book_id, patron_id):
        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break
        else:
            print("Patron not found.")
            return

        for book in patron.borrowed_books:
            if book.book_id == book_id:
                book.is_borrowed = False
                patron.borrowed_books.remove(book)
                print("Book returned successfully.")
                return

        print("This book was not borrowed by this patron.")


# Create library
library = Library()

# Create books
book1 = Book(1, "Python Programming", "John Smith")
book2 = Book(2, "Data Structures", "Robert Brown")

# Add books
library.add_book(book1)
library.add_book(book2)

# Create patrons
patron1 = Patron(101, "Tanushka")

# Register patron
library.register_patron(patron1)

# Borrow book
library.borrow_book(1, 101)

# Return book
library.return_book(1, 101)


      
    
