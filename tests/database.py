from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.main import app

from app.config import settings
from app.database import get_db, Base

SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:1234@localhost:5432/socialapi_test'

# SQLALCHEMY_DATABASE_URL = (
#     f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}"
#     f"@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
# )

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  
  
@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)