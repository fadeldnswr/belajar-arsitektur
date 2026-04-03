'''
Book model using Pydantic for data validation and serialization.
'''
from pydantic import BaseModel
from typing import List, Optional

# Define books metadata
class Book(BaseModel):
  id: int
  title: str
  author: str
  published_year: int
  genre: Optional[str] = None

# Define books response model
class BooksResponse(BaseModel):
  data: List[Book]

# Define message for successful deletion of a book entry
class Message(BaseModel):
  status: int
  message: str
  data: Optional[List] = None


# Define list of books
books: List[Book] = [
  Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", published_year=1925, genre="Novel"),
  Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", published_year=1960, genre="Novel"),
]