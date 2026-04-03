
from src.models.books import BooksResponse, books

# Define class for handling GET /books endpoint
class GetBooksController:
  def __init__(self, book_id: int = None):
    self.book_id = book_id
  
  # Method to retrieve all books from the in-memory list
  def get_books(self) -> BooksResponse:
    return BooksResponse(data=books)
  
  # Method to retrieve a book by its ID
  def get_book_by_id(self) -> BooksResponse:
    for book in books:
      if book.id == self.book_id:
        return BooksResponse(data=[book])