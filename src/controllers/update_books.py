

from src.models.books import Book, BooksResponse, books

# Define class for handling PUT /books/{book_id} endpoint
class UpdateBooksController:
  def __init__(self):
    pass
  
  # Method to update book details
  def update_book(self, book_id: int, updated_book: Book) -> BooksResponse:
    for index, book in enumerate(books):
      if book.id == book_id:
        # Update the book details in the list
        books[index] = updated_book
        break
    return BooksResponse(data=books)