from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Text
from .database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    __table_args__ = {'extend_existing': True}  # Añadir esta línea

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    contraseña = Column(String)
    fecha_creacion = Column(TIMESTAMP)

# Asegúrate de hacer lo mismo para los otros modelos
