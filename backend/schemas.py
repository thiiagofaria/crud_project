from pydantic import BaseModel, PositiveFloat, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class CategoriaBase(Enum):
    categoria1 = "FERRAGENS"
    categoria2 = "FERRAMENTAS"
    categoria3 = "ELÉTRICA"
    categoria4 = "HIDRÁULICA"
    categoria5 = "ACABAMENTO"
    categoria6 = "ESTRUTURA"
    categoria7 = "ISOLAMENTO"
    categoria8 = "SEGURANÇA"

class MaterialBase(BaseModel):
    material: str
    categoria: str
    localização_material: str
    quantidade: PositiveFloat

    @validator("categoria")
    def check_categoria(cls, v):
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria Inválida")

class MaterialCreate(MaterialBase):
    pass

class MaterialResponse(MaterialBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

        
class MaterialUpdate(BaseModel):
    material: Optional[str] = None
    categoria: Optional[str] = None
    localização_material: Optional[str] = None
    quantidade: Optional[PositiveFloat] = None

    @validator("categoria")
    def check_categoria(cls, v):
        if v is None:
            return v
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria Inválida")


