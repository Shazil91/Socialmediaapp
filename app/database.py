from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings


SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}"
    f"@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
)

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency for getting the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# try:
#     conn = psycopg2.connect(host='localhost', database='Socialapi', user='postgres', password='1234',
#                             cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connection was successfull")
# except Exception as error:
#     print("Connecting to database failed")
#     print("Error: ", error)
#     time.sleep(2)
