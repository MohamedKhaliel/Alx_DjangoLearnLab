# CRUD_operations

## Create
```
from bookshel.models import Book 

new_book = Book.objects.create(title = "1984",author = "George Orwell" , publication_year= '1949' )
new_book.save()

# Expected output: <Book: Book object (1)> or similar depending on the primary key
new_book
```
## Read
```
from bookshelf.models import Book
book = Book.objects.get()
book.title # Expected Output: '1984'
book.author # Expected Output: 'George Orwell'
book.publication_year # Expected Output: 1949
```
## Update
```
from library.models import Book

# Retrieve the book by title
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()  # Save the changes to the database

# Expected output: 'Nineteen Eighty-Four', confirming the title has been updated
book.title # Output: 'Nineteen Eighty-Four'
```
## Delete
```
# Import the Book model
from bookshelf.models import Book

# Retrieve the book to be deleted
book_to_delete = Book.objects.get(title='1984')

book_to_delete.delete()
# Expected output: (1, {'library.Book': 1}), indicating one `Book` instance was deleted

# Confirm deletion by retrieving all books

all_books = Book.objects.all()
all_books  # Expected Output: <QuerySet []> if no other books exist, or a list of remaining books
```