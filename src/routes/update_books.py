from fastapi import APIRouter, HTTPException, Query

from src.controllers.update_books import UpdateBooksController
from src.models.books import Book, Message

# Define router for handling book-related endpoints
router = APIRouter(
  prefix="/books",
  tags=["PUT"]
)

# Define endpoint to update a book by its ID
@router.put("/{book_id}", response_model=Message, status_code=200)
async def update_book_by_id(
  book_id: int, title: str = Query(..., description="The title of the book"), 
  author: str = Query(..., description="The author of the book"), published_year: int = Query(..., description="The year the book was published"), 
  genre: str = Query(None, description="The genre of the book" )):
  try:
    # Create an instance of updated books
    controller = UpdateBooksController()
    
    # Create an instance of the updated book with the provided details
    updated_book = Book(
      id=book_id, title=title, author=author, published_year=published_year, genre=genre
    )
    
    # Call the controller method to update the book details
    response = controller.update_book(book_id, updated_book)
    
    # Check if the book ID does not exist in the list of books
    for book in response.data:
      if book.id == book_id:
        break
      else:
        return Message(
          status=404, 
          message=f"Book with ID {book_id} not found", 
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