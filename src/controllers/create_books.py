
from src.schemas.books import BooksResponse, BookCreate
from src.repositories.book_repository import BookRepository

# Define controller for handling POST /books endpoint to create new book entries
class CreateBooksController:
  def __init__(self, repo: BookRepository):
    self.repo = repo

  # Method to create a new book entry
  def create_book(self, new_book: BookCreate) -> BooksResponse:
    book_data = new_book.model_dump()
    create_new_book = self.repo.create(book_data)
    return BooksResponse(data=[create_new_book]) if create_new_book else BooksResponse(data=[])