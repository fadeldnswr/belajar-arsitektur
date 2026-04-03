
from src.models.books import Book, BooksResponse, books

# Define class for handling DELETE /books/{book_id} endpoint
class DeleteBooksController:
  def __init__(self):
    pass
  
  # Method query to delete a book by its ID
  def delete_book(self, book_id: int) -> BooksResponse:
    for index, book in enumerate(books):
      if book.id == book_id:
        del books[index]
        break
      return BooksResponse(data=books)