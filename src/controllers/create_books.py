
from src.models.books import Book, BooksResponse, BookDB
from sqlalchemy.orm import Session

# Define controller for handling POST /books endpoint to create new book entries
class CreateBooksController:
  def __init__(self):
    pass
  
  # Method to create a new book entry
  def create_book(self, new_book: Book, db: Session) -> BooksResponse:
    # Create a new book instance to be added to the database
    book_db = BookDB(
      title=new_book.title,
      author=new_book.author,
      published_year=new_book.published_year,
      genre=new_book.genre
    )
    
    # Add the new book to the database session and commit the transaction
    db.add(book_db)
    db.commit()
    db.refresh(book_db)  # Refresh the instance to get the generated ID and other fields
    
    # Return the created book details in the response
    return BooksResponse(data=[book_db])