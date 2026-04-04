'''
Books schema module defining API response models for book-related endpoints.
'''
import uuid

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict

# Define base books schema for book creation and response models
class BaseBook(BaseModel):
  title: str
  author: str
  published_year: int
  genre: Optional[str] = None

# Define book schema for book creation
class BookCreate(BaseBook):
  pass

# Define book schema for book update
class BookUpdate(BaseBook):
  title: Optional[str] = None
  author: Optional[str] = None
  published_year: Optional[int] = None
  genre: Optional[str] = None

# Define books metadata for the API response
class Book(BaseBook):
  id: uuid.UUID
  created_at: Optional[datetime] = None
  model_config = ConfigDict(from_attributes=True)

# Define books response model
class BooksResponse(BaseModel):
  data: List[Book]

# Define message for successful deletion of a book entry
class Message(BaseModel):
  status: int
  message: str
  data: Optional[List] = None