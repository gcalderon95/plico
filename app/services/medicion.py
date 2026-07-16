# app/services/medicion.py

from sqlalchemy.orm import Session
from app.schemas.medicion import MedicionCorporalCreate
from app.models.modelo import MedicionCorporal, Usuario


def crear_medicion(db: Session, medicion: MedicionCorporalCreate, current_user: Usuario):
    medicion_data = medicion.model_dump()
    nueva_medicion = MedicionCorporal(
        **medicion_data,
        usuario_id=current_user.id
    )
    
    db.add(nueva_medicion)
    db.commit()
    db.refresh(nueva_medicion)
    return nueva_medicion

def get_mediciones_service(db: Session, current_user: Usuario):
    return db.query(MedicionCorporal).filter(MedicionCorporal.usuario_id == current_user.id).all()