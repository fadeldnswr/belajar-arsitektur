from typing import TypeVar, Generic, Type, List, Dict
from sqlalchemy.orm import Session

from src.db.db import Base

# Define a generic type variable for the repository
T = TypeVar("T", bound=Base)

# Define class for base repository
class BaseRepository(Generic[T]):
  def __init__(self, model: Type[T], db: Session):
    self.db = db
    self.model = model
  
  # Method to get all objects
  def get_all(self) -> List[T]:
    return self.db.query(self.model).all()
  
  # Method to create new object
  def create(self, obj: Dict) -> T:
    db_obj = self.model(**obj)
    self.db.add(db_obj)
    self.db.commit()
    self.db.refresh(db_obj)
    return db_obj

  # Method to update object
  def update(self, db_obj: T, obj: Dict) -> T:
    for key, value in obj.items():
      setattr(db_obj, key, value)
    self.db.commit()
    self.db.refresh(db_obj)
    return db_obj
  
  # Method to delete object
  def delete(self, db_obj: T) -> T:
    self.db.delete(db_obj)
    self.db.commit()
    return db_obj