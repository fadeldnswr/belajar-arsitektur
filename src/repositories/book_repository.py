from src.models.books import BookDB
from src.schemas.books import BooksResponse
from src.repositories.base import BaseRepository
from sqlalchemy.orm import Session

# Define class for book repository implementation
class BookRepository(BaseRepository[BookDB]):
  def __init__(self, db: Session):
    super().__init__(model=BookDB, db=db)
  
  # Method to get a book by title
  def get_book_by_title(self, book_title: str) -> BookDB | None:
    return self.db.query(BookDB).filter(BookDB.title == book_title).first()
  
  # Method to get list of all books by title
  def list_of_book_by_title(self, book_title: str) -> BooksResponse:
    books = self.db.query(BookDB).filter(BookDB.title == book_title).first()
    return BooksResponse(data=[books])
  
  # Method to filter books by genre
  def filter_books_by_genre(self, genre: str) -> BooksResponse:
    books = self.db.query(BookDB).filter(BookDB.genre == genre).all()
    return BooksResponse(data=books)