
from sqlalchemy.orm import Session
from src.models.books import Book, BooksResponse, BookDB

# Define class for handling PUT /books/{book_id} endpoint
class UpdateBooksController:
  def __init__(self, db: Session = None):
    self.db = db
  
  # Method to update book details
  def update_book(self, book_title: str, updated_book: Book) -> BooksResponse:
    # Query the database to find the book with specific title
    update_book = self.db.query(BookDB).filter(BookDB.title == book_title).first()
    
    # Check if the book exists in the database
    if not update_book:
      return BooksResponse(data=[])  # Return empty response if book not found
    
    # Update the book details with the provided information
    update_book.title = updated_book.title
    update_book.author = updated_book.author
    update_book.published_year = updated_book.published_year
    update_book.genre = updated_book.genre
    
    # Commit the transaction to save the changes in the database
    self.db.commit()
    self.db.refresh(update_book)  # Refresh the instance to get the updated details
    
    # Return the updated book details in the response
    return BooksResponse(data=[update_book])