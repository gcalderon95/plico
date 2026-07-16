#routes/registro.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.modelo import Usuario
from app.schemas.user import UserCreate
from app.database.conexion import get_db
from app.utils.auth_utils import get_password_hash

router = APIRouter()

@router.post("/registro", status_code=201)
def registro(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(Usuario).filter(Usuario.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    hashed_password = get_password_hash(user.password)
    nuevo_usuario = Usuario(
        nombre=user.nombre,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return {"msg": "Usuario registrado exitosamente"}