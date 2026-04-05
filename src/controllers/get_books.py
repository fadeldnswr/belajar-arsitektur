
from src.schemas.books import BooksResponse
from src.models.books import BookDB
from sqlalchemy.orm import Session
from src.repositories.book_repository import BookRepository

# Define class for handling GET /books endpoint
class GetBooksController:
  # Method to retrieve all books from the in-memory list
  def get_books(self, db: Session) -> BooksResponse:
    repo = BookRepository(db)
    get_all_books_list = repo.get_all()
    return BooksResponse(data=get_all_books_list)
  
  # Method to retrieve a book by its ID
  def get_book_by_title(self, book_title: str, db: Session) -> BooksResponse:
    repo = BookRepository(db)
    return repo.get_book_by_title(book_title)
  
  # Method to get list of all books by title
  def get_books_by_title_list(self, book_title: str, db: Session) -> BooksResponse:
    repo = BookRepository(db)
    return repo.list_of_book_by_title(book_title)
  
  # Method to filter books by genre
  def filter_books_by_genre(self, genre: str, db: Session) -> BooksResponse:
    repo = BookRepository(db)
    return repo.filter_books_by_genre(genre)