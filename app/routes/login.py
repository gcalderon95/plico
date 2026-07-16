from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import timedelta

from app.models.modelo import Usuario
from app.schemas.user import UserLogin
from app.database.conexion import get_db
from app.utils.auth_utils import verify_password, create_access_token

router = APIRouter()

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Email o contraseña incorrectos")

    
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(
        data={"sub": db_user.email}, 
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "usuario": {
            "id": db_user.id,
            "nombre": db_user.nombre,
            "email": db_user.email
        }
    }
