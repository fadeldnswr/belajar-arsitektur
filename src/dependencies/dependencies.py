from fastapi import Depends
from sqlalchemy.orm import Session

from src.db.db import get_db
from src.controllers.get_books import GetBooksController
from src.controllers.create_books import CreateBooksController
from src.controllers.update_books import UpdateBooksController
from src.controllers.delete_books import DeleteBooksController
from src.repositories.book_repository import BookRepository

# Define function to inject dependencies for BookRepository
def get_book_repository(db: Session = Depends(get_db)) -> BookRepository:
  return BookRepository(db)

# Define function to inject dependencies for get books method
def get_books(repo: BookRepository = Depends(get_book_repository)) -> GetBooksController:
  return GetBooksController(repo)

# Define function to inject dependencies for get book by title method
def get_book_by_title(repo: BookRepository = Depends(get_book_repository)) -> GetBooksController:
  return GetBooksController(repo) 

# Define function to inject dependencies for get books by title list method
def get_books_by_title_list(repo: BookRepository = Depends(get_book_repository)) -> GetBooksController:
  return GetBooksController(repo)

# Define function to inject dependencies for filter books by genre method
def filter_books_by_genre(repo: BookRepository = Depends(get_book_repository)) -> GetBooksController:
  return GetBooksController(repo)

# Define function to inject dependencies for create book method
def create_book(repo: BookRepository = Depends(get_book_repository)) -> CreateBooksController:
  return CreateBooksController(repo)

# Define function to inject dependencies for update book method
def update_book(repo: BookRepository = Depends(get_book_repository)) -> UpdateBooksController:
  return UpdateBooksController(repo)  

# Define function to inject dependencies for delete book method
def delete_book(repo: BookRepository = Depends(get_book_repository)) -> DeleteBooksController:
  return DeleteBooksController(repo)