from pydantic import BaseModel, Field
from datetime import datetime

#Notas 
class Note(BaseModel):
    #Creamos una nota(clase) con id integer, titulo string, contenido string y fecha de creacion datetime
    id: int
    title: str
    note_content: str
    creation_date: datetime.now()


class NoteBase(BaseModel):
    title : str = Field(...,min_length=10, max_length=50)
    note_content : str = Field(..., min_length=10)
    creation_date : datetime = Field(default_factory=datetime.now)
    is_completed : bool = Field(default=False)

class NoteCreate(NoteBase):
    content : str #Contenido de la nota, obviamete es un string
    creation_date : datetime = Field(default_factory=datetime.now) #Tomamos la fecha actual al crear la nota

class NoteRead(NoteBase):
    #Esta función solo deberia de tomar el numero entero para buscar la nota por su id
    id : int