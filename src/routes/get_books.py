from fastapi import APIRouter, HTTPException, Depends, Query

from src.controllers.get_books import GetBooksController
from src.dependencies.dependencies import (
  get_books, get_book_by_title, 
  filter_books_by_genre
)
from src.schemas.books import Message

# Define router for handling book-related endpoints
router = APIRouter(
  prefix="/books",
  tags=["GET"]
)

# Endpoint to get all books
@router.get("/", response_model=Message, status_code=200)
async def get_books(controller: GetBooksController = Depends(get_books)):
  try:
    # Define a controller instance to handle the request
    response = controller.get_books()

    # Check if there are no books in the list before returning the response
    if not response.data:
      return Message(
        status=200,
        message="No books found.",
        data=[]
      )
    
    # Return the response from the controller method to get all books
    return Message(
      status=200,
      message="Books retrieved successfully.",
      data=response.data
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

# Endpoint to filter books by genre
@router.get("/genre", response_model=Message, status_code=200)
async def get_books_by_genre(genre: str = Query(..., description="Books genre to filter by"), controller: GetBooksController = Depends(filter_books_by_genre)):
  try:
    # Define a controller instance to handle the request
    response = controller.filter_books_by_genre(genre)
    
    # Check if there are no books with the specified genre
    if not response.data:
      return Message(
        status=200,
        message=f"No books found with genre {genre}.",
        data=[]
      )
    
    # Return the response
    return Message(
      status=200,
      message="Books retrieved successfully.",
      data=response.data
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get books by title
@router.get("/{book_title}", response_model=Message, status_code=200)
async def get_book_by_title(book_title: str, controller: GetBooksController = Depends(get_book_by_title)):
  try:
    # Define a controller instance to handle the request
    response = controller.get_books_by_title_list(book_title)
    
    # Check if there are no books with the specified title in the list before returning the response
    if not response.data:
      return Message(
        status=200,
        message=f"No books found with title {book_title}.",
        data=[]
      )
    
    # Return the response from the controller method to get a book by its title
    return Message(
      status=200,
      message="Book retrieved successfully.",
      data=response.data
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))