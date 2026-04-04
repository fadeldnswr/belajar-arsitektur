'''
Book model using Pydantic for data validation and serialization.
'''
import uuid 

from pydantic import BaseModel
from typing import List, Optional
from src.db.db import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

# Define books metadata
class Book(BaseModel):
  id: uuid.UUID
  title: str
  author: str
  published_year: int
  genre: Optional[str] = None
  created_at: Optional[datetime] = None
  
  class Config:
    from_attributes = True

# Define books response model
class BooksResponse(BaseModel):
  data: List[Book]
  
  class Config:
    from_attributes = True

# Define message for successful deletion of a book entry
class Message(BaseModel):
  status: int
  message: str
  data: Optional[List] = None

# Define database schema for books
class BookDB(Base):
  __tablename__ = "books" # Table name in the database
  
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
  title = Column(String, index=True)
  author = Column(String, index=True)
  published_year = Column(Integer)
  genre = Column(String, index=True)
  created_at = Column(DateTime, default=datetime.now(), server_default=func.now())