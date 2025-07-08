from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# 🔹 Dépendance DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Élève
@app.post("/eleves/")
def create_eleve(eleve: schemas.EleveCreate, db: Session = Depends(get_db)):
    return crud.create_eleve(db, eleve)


@app.get("/eleves/")
def read_eleves(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_eleves(db, skip=skip, limit=limit)


@app.get("/eleves/{eleve_id}")
def read_eleve(eleve_id: int, db: Session = Depends(get_db)):
    eleve = crud.get_eleve(db, eleve_id)
    if not eleve:
        raise HTTPException(status_code=404, detail="Élève non trouvé")
    return eleve


@app.put("/eleves/{eleve_id}")
def update_eleve(eleve_id: int, eleve: schemas.EleveCreate, db: Session = Depends(get_db)):
    db_eleve = crud.update_eleve(db, eleve_id, eleve)
    if not db_eleve:
        raise HTTPException(status_code=404, detail="Élève non trouvé")
    return db_eleve


@app.delete("/eleves/{eleve_id}")
def delete_eleve(eleve_id: int, db: Session = Depends(get_db)):
    db_eleve = crud.delete_eleve(db, eleve_id)
    if not db_eleve:
        raise HTTPException(status_code=404, detail="Élève non trouvé")
    return {"detail": "Élève supprimé"}


# Matière
@app.post("/matieres/")
def create_matiere(matiere: schemas.MatiereCreate, db: Session = Depends(get_db)):
    return crud.create_matiere(db, matiere)


@app.get("/matieres/")
def read_matieres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_matieres(db, skip=skip, limit=limit)


@app.get("/matieres/{matiere_id}")
def read_matiere(matiere_id: int, db: Session = Depends(get_db)):
    matiere = crud.get_matiere(db, matiere_id)
    if not matiere:
        raise HTTPException(status_code=404, detail="Matière non trouvée")
    return matiere


@app.put("/matieres/{matiere_id}")
def update_matiere(matiere_id: int, matiere: schemas.MatiereCreate, db: Session = Depends(get_db)):
    db_matiere = crud.update_matiere(db, matiere_id, matiere)
    if not db_matiere:
        raise HTTPException(status_code=404, detail="Matière non trouvée")
    return db_matiere


@app.delete("/matieres/{matiere_id}")
def delete_matiere(matiere_id: int, db: Session = Depends(get_db)):
    db_matiere = crud.delete_matiere(db, matiere_id)
    if not db_matiere:
        raise HTTPException(status_code=404, detail="Matière non trouvée")
    return {"detail": "Matière supprimée"}


# examen
@app.post("/examens/")
def create_examen(examen: schemas.ExamenCreate, db: Session = Depends(get_db)):
    return crud.create_examen(db, examen)


@app.get("/examens/")
def read_examens(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_examens(db, skip=skip, limit=limit)


@app.get("/examens/{examen_id}")
def read_examen(examen_id: int, db: Session = Depends(get_db)):
    examen = crud.get_examen(db, examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen non trouvé")
    return examen


@app.put("/examens/{examen_id}")
def update_examen(examen_id: int, examen: schemas.ExamenCreate, db: Session = Depends(get_db)):
    db_examen = crud.update_examen(db, examen_id, examen)
    if not db_examen:
        raise HTTPException(status_code=404, detail="Examen non trouvé")
    return db_examen


@app.delete("/examens/{examen_id}")
def delete_examen(examen_id: int, db: Session = Depends(get_db)):
    db_examen = crud.delete_examen(db, examen_id)
    if not db_examen:
        raise HTTPException(status_code=404, detail="Examen non trouvé")
    return {"detail": "Examen supprimé"}


# Notes
@app.post("/notes/")
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note)


@app.get("/notes/")
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_notes(db, skip=skip, limit=limit)


@app.get("/notes/{note_id}")
def read_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note non trouvée")
    return note


@app.put("/notes/{note_id}")
def update_note(note_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)):
    db_note = crud.update_note(db, note_id, note)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note non trouvée")
    return db_note


@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.delete_note(db, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note non trouvée")
    return {"detail": "Note supprimée"}
