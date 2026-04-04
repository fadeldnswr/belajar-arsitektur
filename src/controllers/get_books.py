
from src.models.books import BooksResponse, BookDB
from sqlalchemy.orm import Session

# Define class for handling GET /books endpoint
class GetBooksController:
  def __init__(self, db: Session = None):
    self.db = db
  
  # Method to retrieve all books from the in-memory list
  def get_books(self) -> BooksResponse:
    # Query all books from the database
    books = self.db.query(BookDB).all() 
    return BooksResponse(data=books) # Return the list of books in the response
  
  # Method to retrieve a book by its ID
  def get_book_by_title(self, book_title: str) -> BooksResponse:
    # Query the database to find the book with the specified title
    books = self.db.query(BookDB).filter(BookDB.title == book_title).all()
    return BooksResponse(data=books) # Return the book details in the response
  
  # Method to filter books by genre
  def filter_books_by_genre(self, genre: str) -> BooksResponse:
    # Query the database to find books with the specified genre
    books = self.db.query(BookDB).filter(BookDB.genre == genre).all()
    return BooksResponse(data=books) # Return the filtered list of books in the response