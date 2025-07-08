from pydantic import BaseModel
from datetime import date
from typing import Optional


# eleve
class EleveBase(BaseModel):
    nom: str
    prenom: str
    classe: str

class EleveCreate(EleveBase):
    pass

class EleveOut(EleveBase):
    id: int

    class Config:
        orm_mode = True


# Matière
class MatiereBase(BaseModel):
    nom: str

class MatiereCreate(MatiereBase):
    pass

class MatiereOut(MatiereBase):
    id: int

    class Config:
        orm_mode = True


# Examen
class ExamenBase(BaseModel):
    date: date
    matiere_id: int

class ExamenCreate(ExamenBase):
    pass

class ExamenOut(ExamenBase):
    id: int

    class Config:
        orm_mode = True


# note
class NoteBase(BaseModel):
    valeur: float
    eleve_id: int
    examen_id: int
    matiere_id: int

class NoteCreate(NoteBase):
    pass

class NoteOut(NoteBase):
    id: int

    class Config:
        orm_mode = True
