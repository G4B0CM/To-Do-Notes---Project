import os
from dotenv import load_dotenv

from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from fastapi import Depends

from to_do_project.application.interfaces.i_note_repository import INoteRepository
from to_do_project.application.use_cases.crud_note_use_case import CrudNoteUseCase
from to_do_project.infrastructure.database.repositories.note_repository import NoteRepository
from to_do_project.infrastructure.database.models.note_model import Base

load_dotenv()

DATABASE_URL= os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("El campo DATABASE_URL no se encontró en la variables de entorno")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def get_notes_repository(db : Session = Depends(get_db)) -> INoteRepository:
    return NoteRepository(db=db)

def get_note_use_case(note_repo : INoteRepository = Depends(get_notes_repository)) -> CrudNoteUseCase:
    return CrudNoteUseCase(note_repo=note_repo)
