from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..models import Categoria, CategoriaBase, CategoriaRead
from ..database import get_session

router = APIRouter(prefix="/categorias", tags=["categorias"])

@router.post("/", response_model=CategoriaRead)
def crear_categoria(categoria: CategoriaBase, session: Session = Depends(get_session)):
    nueva = Categoria(**categoria.model_dump())
    session.add(nueva)
    session.commit()
    session.refresh(nueva)
    return nueva

@router.get("/", response_model=list[CategoriaRead])
def listar_categorias(session: Session = Depends(get_session)):
    categorias = session.exec(select(Categoria)).all()
    return categorias
