from sqlalchemy.orm import Session
from models import Eleve, Matiere, Examen, Note
import schemas


# 🔹 CRUD Élève
def get_eleve(db: Session, eleve_id: int):
    return db.query(Eleve).filter(Eleve.id == eleve_id).first()

def get_eleves(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Eleve).offset(skip).limit(limit).all()

def create_eleve(db: Session, eleve: schemas.EleveCreate):
    db_eleve = Eleve(**eleve.dict())
    db.add(db_eleve)
    db.commit()
    db.refresh(db_eleve)
    return db_eleve

def update_eleve(db: Session, eleve_id: int, eleve_update: schemas.EleveCreate):
    eleve = get_eleve(db, eleve_id)
    if eleve:
        for key, value in eleve_update.dict().items():
            setattr(eleve, key, value)
        db.commit()
        db.refresh(eleve)
    return eleve

def delete_eleve(db: Session, eleve_id: int):
    eleve = get_eleve(db, eleve_id)
    if eleve:
        db.delete(eleve)
        db.commit()
    return eleve


# 🔹 CRUD Matière
def get_matiere(db: Session, matiere_id: int):
    return db.query(Matiere).filter(Matiere.id == matiere_id).first()

def get_matieres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Matiere).offset(skip).limit(limit).all()

def create_matiere(db: Session, matiere: schemas.MatiereCreate):
    db_matiere = Matiere(**matiere.dict())
    db.add(db_matiere)
    db.commit()
    db.refresh(db_matiere)
    return db_matiere

def update_matiere(db: Session, matiere_id: int, matiere_update: schemas.MatiereCreate):
    matiere = get_matiere(db, matiere_id)
    if matiere:
        for key, value in matiere_update.dict().items():
            setattr(matiere, key, value)
        db.commit()
        db.refresh(matiere)
    return matiere

def delete_matiere(db: Session, matiere_id: int):
    matiere = get_matiere(db, matiere_id)
    if matiere:
        db.delete(matiere)
        db.commit()
    return matiere


# 🔹 CRUD Examen
def get_examen(db: Session, examen_id: int):
    return db.query(Examen).filter(Examen.id == examen_id).first()

def get_examens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Examen).offset(skip).limit(limit).all()

def create_examen(db: Session, examen: schemas.ExamenCreate):
    db_examen = Examen(**examen.dict())
    db.add(db_examen)
    db.commit()
    db.refresh(db_examen)
    return db_examen

def update_examen(db: Session, examen_id: int, examen_update: schemas.ExamenCreate):
    examen = get_examen(db, examen_id)
    if examen:
        for key, value in examen_update.dict().items():
            setattr(examen, key, value)
        db.commit()
        db.refresh(examen)
    return examen

def delete_examen(db: Session, examen_id: int):
    examen = get_examen(db, examen_id)
    if examen:
        db.delete(examen)
        db.commit()
    return examen


# 🔹 CRUD Note
def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Note).offset(skip).limit(limit).all()

def create_note(db: Session, note: schemas.NoteCreate):
    db_note = Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note(db: Session, note_id: int, note_update: schemas.NoteCreate):
    note = get_note(db, note_id)
    if note:
        for key, value in note_update.dict().items():
            setattr(note, key, value)
        db.commit()
        db.refresh(note)
    return note

def delete_note(db: Session, note_id: int):
    note = get_note(db, note_id)
    if note:
        db.delete(note)
        db.commit()
    return note
