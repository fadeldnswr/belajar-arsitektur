from fastapi import APIRouter, HTTPException, Query, Depends
from src.schemas.books import BookUpdate, Message

from src.controllers.update_books import UpdateBooksController
from src.dependencies.dependencies import update_book

# Define router for handling book-related endpoints
router = APIRouter(
  prefix="/books",
  tags=["PUT"]
)

# Define endpoint to update a book by its title
@router.put("/", response_model=Message, status_code=200)
async def update_book_by_id(
  new_book: BookUpdate, book_title: str = Query(..., description="Title of the book to be updated"), 
  controller: UpdateBooksController = Depends(update_book)):
  try:
    # Call the controller method to update the book details
    response = controller.update_book(book_title, new_book)
    
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