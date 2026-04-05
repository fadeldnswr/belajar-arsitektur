
from src.repositories.book_repository import BookRepository
from src.schemas.books import BooksResponse
from sqlalchemy.orm import Session

# Define class for handling DELETE /books/{book_id} endpoint
class DeleteBooksController:
  # Method to delete a book by its title
  def delete_book(self, book_title: str, db: Session) -> BooksResponse:
    repo = BookRepository(db)
    current_book_data = repo.get_book_by_title(book_title)
    
    # Check if the book with the specified title exists before attempting to delete it
    if not current_book_data:
      return BooksResponse(data=[])
    
    # Delete the book and return the deleted book details in the response
    deleted_book = repo.delete(current_book_data)
    
    # Return the deleted book details in the response if the deletion was successful, otherwise return an empty list
    return BooksResponse(data=[deleted_book]) if deleted_book else BooksResponse(data=[])