
from fastapi import APIRouter, HTTPException, Depends
from src.controllers.get_books import GetBooksController
from src.models.books import Message

# Define router for handling book-related endpoints
router = APIRouter(
  prefix="/books",
  tags=["GET"]
)

# Define function to get all books
def get_all_books():
  return GetBooksController()

# Endpoint to get all books
@router.get("/", response_model=Message, status_code=200)
async def get_books(get_all_books: GetBooksController = Depends(get_all_books)):
  try:
    # Define a controller instance to handle the request
    controller = get_all_books.get_books()
    response = controller.data
    
    # Return the response from the controller method to get all books
    return Message(
      status=200,
      message="Books retrieved successfully.",
      data=response
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get books by ID
@router.get("/{book_id}", response_model=Message, status_code=200)
async def get_book_by_id(book_id: int):
  try:
    # Define a controller instance to handle the request
    controller = GetBooksController(book_id=book_id)
    response = controller.get_book_by_id()
    
    # Return the response from the controller method to get a book by its ID
    return Message(
      status=200,
      message="Book retrieved successfully.",
      data=[response] if response else []
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))