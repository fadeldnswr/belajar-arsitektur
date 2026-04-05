from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db.db import Base, engine
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

# Configure CORS middleware to allow requests from any origin
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"]
)

# Include routers for book-related endpoints
app.include_router(get_books.router)
app.include_router(create_books.router)
app.include_router(delete_books.router)
app.include_router(update_books.router)

# Create base metadata for database models
Base.metadata.create_all(bind=engine)

# Define root endpoint
@app.get("/")
async def root():
  return {"message": "Welcome to the Books API!"}