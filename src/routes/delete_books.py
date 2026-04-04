import uuid
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.controllers.delete_books import DeleteBooksController
from src.models.books import Message
from src.db.db import get_db

# Define router for handling book-related endpoints
router = APIRouter(
  prefix="/books",
  tags=["DELETE"]
)

# Define endpoint to delete a book by its title
@router.delete("/{book_title}", response_model=Message, status_code=200)
async def delete_book(book_title: str, db: Session = Depends(get_db)):
  try:
    # Define a controller instance to handle the request
    controller = DeleteBooksController(db=db)
    response = controller.delete_book(book_title)
    
    # Check if the book title doesn't exist in the list of books before attempting to delete
    if not response.data:
      return Message(
        status=404,
        message=f"Book with title {book_title} not found.",
        data=None
      )
    
    # Return the response from the controller method to delete a book entry by its title
    return Message(
      status=200, 
      message=f"Book with title {book_title} deleted successfully."
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))