from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from app.config import DATABASE_URL
from app.repositories.orm import Base

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    """
    Crea una nueva sesión de base de datos.
    Se debe utilizar con 'yield' en un 'with' para asegurar que se cierre correctamente.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """
    Crea las tablas en la base de datos si no existen.
    Esta función es útil cuando la base de datos es inicializada o cuando se necesitan crear tablas por primera vez.
    """
    try:
        Base.metadata.create_all(bind=engine)
        print("Base de datos inicializada correctamente.")
    except SQLAlchemyError as e:
        print(f"Error al inicializar la base de datos: {e}")
