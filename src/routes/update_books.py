from fastapi import APIRouter, HTTPException, Query, Depends
from src.models.books import Book, Message, BookDB
from sqlalchemy.orm import Session

from src.db.db import get_db
from src.controllers.update_books import UpdateBooksController
from src.db.db import get_db

# Define router for handling book-related endpoints
router = APIRouter(
  prefix="/books",
  tags=["PUT"]
)

# Define endpoint to update a book by its title
@router.put("/", response_model=Message, status_code=200)
async def update_book_by_id(new_book: Book, db: Session = Depends(get_db), book_title: str = Query(..., description="Title of the book to be updated")):
  try:
    # Create an instance of updated books
    controller = UpdateBooksController(db=db)
    
    # Create an instance of the updated book with the provided details
    updated_book = BookDB(
      id=new_book.id, title=new_book.title, author=new_book.author, 
      published_year=new_book.published_year, genre=new_book.genre
    )
    
    # Call the controller method to update the book details
    response = controller.update_book(book_title, updated_book)
    
    # Check if the book with the specified title doesn't exist
    if not response.data:
      return Message(
        status=404,
        message=f"Book with title {book_title} not found.",
        data=None
      )
    
    # Return a success message with the updated list of books
    return Message(
      status=200, 
      message="Book updated successfully", 
      data=response.data
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))