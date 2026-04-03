
from fastapi import APIRouter, HTTPException, Query
from src.controllers.create_books import CreateBooksController
from src.models.books import BooksResponse, Book, Message

# Define router for handling book-related endpoints
router = APIRouter(
  prefix="/books",
  tags=["POST"]
)

# Endpoint to create a new book entry
@router.post("/", response_model=Message, status_code=201)
async def create_book(
  id: int = Query(..., description="The unique ID of the book"), title: str = Query(..., description="The title of the book"),
  author: str = Query(..., description="The author of the book"), published_year: int = Query(..., description="The year the book was published"),
  genre: str = Query(..., description="The genre of the book")) -> Message:

  try:
    # Insert the new book details into a Book model instance
    controller = CreateBooksController()
    
    # New book instance to be created
    new_book = Book(
      id=id, title=title, author=author,
      published_year=published_year, genre=genre,
    )
    
    # Call the controller method to create a new book entry and get the response
    response = controller.create_book(new_book)
    
    # Check if the book ID already exists in the list of books
    for book in response.data:
      if book.id == id:
        return Message(
          status=400, 
          message=f"Book with ID {id} already exists", 
          data=None
        )
    
    # Return the response from the controller method to create a new book entry
    return Message(
      status=201, 
      message="Book created successfully", 
      data=response.data
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))