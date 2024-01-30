from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    contraseña: str

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

    class Config:
        orm_mode = True
