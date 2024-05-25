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

class ProductBase(BaseModel):
    material: str
    categoria: str
    localização_material: str
    quantidade: PositiveFloat

    @validator("categoria")
    def check_categoria(cls, v)
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria Inválida")

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

        


