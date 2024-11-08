from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Using the related_name to access books of an author
    for book in books:
        print(f"Book Title: {book.title}")

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Access books related to the library
    for book in books:
        print(f"Book Title: {book.title}")

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Using the related_name of the OneToOneField
    print(f"Librarian: {librarian.name}")

# Sample function calls
if __name__ == "__main__":
    # Test: Get all books by a specific author
    get_books_by_author("J.K. Rowling")
    
    # Test: List all books in a specific library
    get_books_in_library("Central Library")
    
    # Test: Get the librarian of a specific library
    get_librarian_for_library("Central Library")
