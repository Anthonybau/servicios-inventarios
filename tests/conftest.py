import pytest
from sqlmodel import SQLModel, create_engine, Session
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_session
from app import models  # importa tus modelos para que se registren

@pytest.fixture(name="session")
def session_fixture():
    # Creamos engine y sesión sobre SQLite en memoria
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})

    # 💡 Muy importante: crear las tablas aquí
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):
    # Inyectamos la sesión de prueba en la app
    def override_get_session():
        yield session
    app.dependency_overrides[get_session] = override_get_session
    return TestClient(app)
