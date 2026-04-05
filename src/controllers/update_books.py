
from src.schemas.books import BooksResponse, BookUpdate
from sqlalchemy.orm import Session
from src.repositories.book_repository import BookRepository

# Define class for handling PUT /books/{book_id} endpoint
class UpdateBooksController:
  def __init__(self, repo: BookRepository):
    self.repo = repo
  
  # Method to update book details
  def update_book(self, book_title: str, updated_book: BookUpdate) -> BooksResponse:
    current_book_data = self.repo.get_book_by_title(book_title)
    update_book_repo = self.repo.update(current_book_data, updated_book.model_dump(exclude_unset=True))
    return BooksResponse(data=[update_book_repo]) if update_book_repo else BooksResponse(data=[])