from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from hotel.db.models import Base
from ..main import app
from hotel.db.engine import init_db

SQLALCHEMY_DB_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[init_db] = override_get_db

client = TestClient(app)

def test_create_customer():
    pass