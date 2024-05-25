from sqlalchemy import Column, INTEGER, String,  FLOAT, DateTime
from sqlalchemy.sql import func
from database import Base

class estoque(Base):
    __tablename__ = "estoque" # nome da tabela

    id = Column(INTEGER, primary_key=True, index=True)
    material = Column(String)
    categoria = Column(String)
    localização_material = Column(String)
    quantidade = Column(INTEGER)
    created_at = Column(DateTime(timezone=True), default=func.now())