from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.db.config import settings

# Load database settings
DATABASE_URL = settings.DATABASE_URL

# Create SQLAlchemy engine
engine = create_engine(
  DATABASE_URL, connect_args={
    "check_same_thread": False # Required for SQLite to allow multiple threads to access the database
  }
)

# Create a configured "Session" class
SessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine
)

# Create a base class for declarative class definitions
class Base(DeclarativeBase):
  pass

# Dependency to get a database session
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()