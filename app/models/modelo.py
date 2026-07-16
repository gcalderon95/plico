# app/models/models.py

from sqlalchemy import Column, Integer, String, Text, Date, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum as PyEnum

# Importar la Base declarativa desde tu archivo database.py
from app.database.conexion import Base

# Importar el tipo ENUM específico de PostgreSQL
from sqlalchemy.dialects.postgresql import ENUM as PGEnum

# --- Definición de tus Enums de Python ---
class TipoComidaEnum(PyEnum):
    DESAYUNO = "desayuno"
    ALMUERZO = "almuerzo"
    CENA = "cena"
    SNACK = "snack"

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True) # Ejemplo de campo
    email = Column(String, unique=True, index=True) # Ejemplo de campo
    hashed_password = Column(String) # Ejemplo de campo

    comidas = relationship("Comida", back_populates="usuario")
    mediciones_corporales = relationship("MedicionCorporal", back_populates="usuario")
    

class Alimento(Base):
    __tablename__ = "alimentos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True) # Ejemplo de campo
    calorias = Column(Integer) # Ejemplo de campo

    comidas_alimentos = relationship("ComidaAlimento", back_populates="alimento")

class Comida(Base):
    __tablename__ = "comidas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    tipo_comida = Column(PGEnum(TipoComidaEnum, name='tipo_comida_enum'))
    notas = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    usuario = relationship("Usuario", back_populates="comidas")
    comidas_alimentos = relationship("ComidaAlimento", back_populates="comida")

class ComidaAlimento(Base):
    __tablename__ = "comidas_alimentos" # Corregido: "alimentos"

    id = Column(Integer, primary_key=True, index=True)
    alimento_id = Column(Integer, ForeignKey("alimentos.id"), nullable=False)
    comida_id = Column(Integer, ForeignKey("comidas.id"), nullable=False)
    cantidad_g = Column(DECIMAL(7,2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    alimento = relationship("Alimento", back_populates="comidas_alimentos")
    comida = relationship("Comida", back_populates="comidas_alimentos")


class MedicionCorporal(Base):
    __tablename__ = "mediciones_corporales"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha = Column(Date, nullable=False)

    # Datos generales
    peso = Column(DECIMAL(5, 2))
    altura = Column(DECIMAL(5, 2))  # cm
    imc = Column(DECIMAL(4, 2))  # opcional, se puede calcular

    # Perímetros (cm)
    cuello = Column(DECIMAL(5, 2))
    hombros = Column(DECIMAL(5, 2))
    pecho = Column(DECIMAL(5, 2))
    cintura = Column(DECIMAL(5, 2))
    cadera = Column(DECIMAL(5, 2))
    brazo_der_relajado = Column(DECIMAL(5, 2))
    brazo_izq_relajado = Column(DECIMAL(5, 2))
    brazo_der_flexionado = Column(DECIMAL(5, 2))
    brazo_izq_flexionado = Column(DECIMAL(5, 2))
    antebrazo_der = Column(DECIMAL(5, 2))
    antebrazo_izq = Column(DECIMAL(5, 2))
    muslo_der = Column(DECIMAL(5, 2))
    muslo_izq = Column(DECIMAL(5, 2))
    pantorrilla_der = Column(DECIMAL(5, 2))
    pantorrilla_izq = Column(DECIMAL(5, 2))

    # Pliegues cutáneos (mm)
    pliegue_bicipital_der = Column(DECIMAL(4, 2))
    pliegue_bicipital_izq = Column(DECIMAL(4, 2))
    pliegue_tricipital_der = Column(DECIMAL(4, 2))
    pliegue_tricipital_izq = Column(DECIMAL(4, 2))
    pliegue_subescapular = Column(DECIMAL(4, 2))
    pliegue_suprailiaco = Column(DECIMAL(4, 2))
    pliegue_abdominal = Column(DECIMAL(4, 2))
    pliegue_muslo_der = Column(DECIMAL(4, 2))
    pliegue_muslo_izq = Column(DECIMAL(4, 2))
    pliegue_pantorrilla_der = Column(DECIMAL(4, 2))
    pliegue_pantorrilla_izq = Column(DECIMAL(4, 2))

    # Otros
    notas = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    usuario = relationship("Usuario", back_populates="mediciones_corporales")
