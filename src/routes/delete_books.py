from fastapi import APIRouter, HTTPException

from src.controllers.delete_books import DeleteBooksController
from src.models.books import Message

# Define router for handling book-related endpoints
router = APIRouter(
  prefix="/books",
  tags=["DELETE"]
)

# Define endpoint to delete a book by its ID
@router.delete("/{book_id}", response_model=Message, status_code=200)
async def delete_book(book_id: int):
  try:
    # Define a controller instance to handle the request
    controller = DeleteBooksController()
    
    # Check if the book ID doesn't exist in the list of books before attempting to delete
    for book in controller.delete_book(book_id).data:
      if book.id == book_id:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found.")
    
    # Return the response from the controller method to delete a book entry by its ID
    return Message(
      status=200, 
      message=f"Book with ID {book_id} deleted successfully."
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))