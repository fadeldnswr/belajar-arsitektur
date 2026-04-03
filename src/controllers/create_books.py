
from src.models.books import Book, BooksResponse, books

# Define controller for handling POST /books endpoint to create new book entries
class CreateBooksController:
  def __init__(self):
    pass
  
  # Method to create a new book entry
  def create_book(self, new_book: Book) -> BooksResponse:
    # Add the new book to the in-memory list of books
    books.append(new_book)
    return BooksResponse(data=books)