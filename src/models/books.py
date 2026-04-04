'''
Book model using Pydantic for data validation and serialization.
'''
import uuid 

from src.db.db import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

# Define base database schema for books
class BookDB(Base):
  __tablename__ = "books" # Table name in the database
  
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
  title = Column(String, index=True)
  author = Column(String, index=True)
  published_year = Column(Integer)
  genre = Column(String, index=True)
  created_at = Column(DateTime, default=datetime.now(), server_default=func.now())