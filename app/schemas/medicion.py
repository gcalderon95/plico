from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class MedicionCorporalBase(BaseModel):
    fecha: date

    # Datos generales
    peso: Optional[float] = None
    altura: Optional[float] = None
    imc: Optional[float] = None

    # Perímetros (cm)
    cuello: Optional[float] = None
    hombros: Optional[float] = None
    pecho: Optional[float] = None
    cintura: Optional[float] = None
    cadera: Optional[float] = None
    brazo_der_relajado: Optional[float] = None
    brazo_izq_relajado: Optional[float] = None
    brazo_der_flexionado: Optional[float] = None
    brazo_izq_flexionado: Optional[float] = None
    antebrazo_der: Optional[float] = None
    antebrazo_izq: Optional[float] = None
    muslo_der: Optional[float] = None
    muslo_izq: Optional[float] = None
    pantorrilla_der: Optional[float] = None
    pantorrilla_izq: Optional[float] = None

    # Pliegues cutáneos (mm)
    pliegue_bicipital_der: Optional[float] = None
    pliegue_bicipital_izq: Optional[float] = None
    pliegue_tricipital_der: Optional[float] = None
    pliegue_tricipital_izq: Optional[float] = None
    pliegue_subescapular: Optional[float] = None
    pliegue_suprailiaco: Optional[float] = None
    pliegue_abdominal: Optional[float] = None
    pliegue_muslo_der: Optional[float] = None
    pliegue_muslo_izq: Optional[float] = None
    pliegue_pantorrilla_der: Optional[float] = None
    pliegue_pantorrilla_izq: Optional[float] = None

    # Otros
    notas: Optional[str] = None

class MedicionCorporalCreate(MedicionCorporalBase):
    pass

class MedicionCorporalUpdate(MedicionCorporalBase):
    pass

class MedicionCorporal(MedicionCorporalBase):
    id: int
    usuario_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
