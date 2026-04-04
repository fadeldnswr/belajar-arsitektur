
import uuid

from src.models.books import Book, BooksResponse, BookDB
from sqlalchemy.orm import Session

# Define class for handling DELETE /books/{book_id} endpoint
class DeleteBooksController:
  def __init__(self, db: Session):
    self.db = db
  
  # Method query to delete a book by its title
  def delete_book(self, book_title: str) -> BooksResponse:
    # Query the database to find the book with specific title
    book = self.db.query(BookDB).filter(BookDB.title == book_title).first()
    
    # Check if the book exists in the database
    if not book:
      return BooksResponse(data=[])  # Return empty response if book not found
    
    # Delete the book from the database and commit the transaction
    self.db.delete(book)
    self.db.commit()
    
    # Return the details of the deleted book in the response
    return BooksResponse(data=[book])