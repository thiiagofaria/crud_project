from sqlalchemy.orm import session
from schemas import MaterialUpdate, MaterialCreate
from models import estoque

def get_item(db: session, estoque_id: int):
    """
    Função que retorna todos os elementos
    """
    return db.query(estoque).filter(estoque.id == estoque_id).first()

def get_item(db: session):
    """
    Função que retorna todos os elementos
    """
    return db.query(estoque).all()

def create_item(db: session, item: MaterialCreate):
    db_material = MaterialCreate(**item.model_dump())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def delete_material(db: session, estoque_id: int):
    db_product = db.query(estoque).filter(estoque.id == estoque_id).first()
    db.delete(db_product)
    db.commit()
    return db_product

def update_material(db: session, estoque_id: int, material: MaterialUpdate):
    db_material = db.query(estoque).filter(estoque.id == estoque_id).first()

    if db_material is None:
        return None

    if material.material is not None:
        db_material.material = material.material
    if material.categoria is not None:
        db_material.categoria = material.categoria
    if material.localização_material is not None:
        db_material.localização_material = material.localização_material
    if material.quantidade is not None:
        db_material.quantidade = material.quantidade

    db.commit()
    return db_material