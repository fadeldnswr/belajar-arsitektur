
from fastapi import APIRouter, HTTPException, Depends
from src.controllers.create_books import CreateBooksController
from src.dependencies.dependencies import create_book
from src.schemas.books import BookCreate, Message

# Define router for handling book-related endpoints
router = APIRouter(
  prefix="/books",
  tags=["POST"]
)

# Endpoint to create a new book entry
@router.post("/", response_model=Message, status_code=201)
async def create_book(new_book: BookCreate, controller: CreateBooksController = Depends(create_book)) -> Message:
  try:
    # Call the controller method to create a new book entry and get the response
    response = controller.create_book(new_book)
    
    # Return the response from the controller method to create a new book entry
    return Message(
      status=201, 
      message="Book has been created successfully", 
      data=response.data
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))