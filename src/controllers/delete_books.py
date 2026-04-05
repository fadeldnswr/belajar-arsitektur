
from src.repositories.book_repository import BookRepository
from src.schemas.books import BooksResponse

# Define class for handling DELETE /books/{book_id} endpoint
class DeleteBooksController:
  def __init__(self, repo: BookRepository):
    self.repo = repo
  
  # Method to delete a book by its title
  def delete_book(self, book_title: str) -> BooksResponse:
    current_book_data = self.repo.get_book_by_title(book_title)
    
    # Check if the book with the specified title exists before attempting to delete it
    if not current_book_data:
      return BooksResponse(data=[])
    
    # Delete the book and return the deleted book details in the response
    deleted_book = self.repo.delete(current_book_data)
    
    # Return the deleted book details in the response if the deletion was successful, otherwise return an empty list
    return BooksResponse(data=[deleted_book]) if deleted_book else BooksResponse(data=[])