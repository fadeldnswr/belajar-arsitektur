from fastapi import FastAPI, HTTPException
from src.routes import (
  get_books, create_books, 
  delete_books, update_books
)


# Define FastAPI app
app = FastAPI(
  title="Books API",
  description="A simple API to manage books",
  version="1.0.0"
)

# Include routers for book-related endpoints
app.include_router(get_books.router)
app.include_router(create_books.router)
app.include_router(delete_books.router)
app.include_router(update_books.router)

# Define root endpoint
@app.get("/")
async def root():
  return {"message": "Welcome to the Books API!"}