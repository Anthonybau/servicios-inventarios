from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..models import Producto, ProductoCreate, ProductoRead
from ..database import get_session

router = APIRouter(prefix="/productos", tags=["productos"])

@router.post("/", response_model=ProductoRead)
def crear_producto(producto: ProductoCreate, session: Session = Depends(get_session)):
    nuevo = Producto(**producto.model_dump())
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[ProductoRead])
def listar_productos(session: Session = Depends(get_session)):
    productos = session.exec(select(Producto)).all()
    return productos

@router.get("/{producto_id}", response_model=ProductoRead)
def obtener_producto(producto_id: int, session: Session = Depends(get_session)):
    producto = session.get(Producto, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto
