from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.medicion import MedicionCorporalCreate, MedicionCorporal
from app.services.medicion import crear_medicion, get_mediciones_service
from app.database.conexion import get_db
from app.utils.auth_utils import get_current_user
from app.models.modelo import Usuario

router = APIRouter()

@router.post("/mediciones/")
def crear_medicion_ruta(
    medicion: MedicionCorporalCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    return crear_medicion(db, medicion, current_user)

@router.get("/mediciones/",response_model=list[MedicionCorporal])
def get_mediciones(db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return get_mediciones_service(db, current_user)
