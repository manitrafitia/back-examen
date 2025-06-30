from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Eleve(Base):
    __tablename__ = "eleves"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    classe = Column(String(50), nullable=False)

    notes = relationship("Note", back_populates="eleve")

class Matiere(Base):
    __tablename__ = "matieres"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)

    examens = relationship("Examen", back_populates="matiere")
    notes = relationship("Note", back_populates="matiere")

class Examen(Base):
    __tablename__ = "examens"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    matiere_id = Column(Integer, ForeignKey("matieres.id"))

    matiere = relationship("Matiere", back_populates="examens")
    notes = relationship("Note", back_populates="examen")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    eleve_id = Column(Integer, ForeignKey("eleves.id"))
    examen_id = Column(Integer, ForeignKey("examens.id"))
    matiere_id = Column(Integer, ForeignKey("matieres.id")) 
    valeur = Column(Float, nullable=False)

    eleve = relationship("Eleve", back_populates="notes")
    examen = relationship("Examen", back_populates="notes")
    matiere = relationship("Matiere", back_populates="notes")
