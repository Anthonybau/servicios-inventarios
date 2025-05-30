from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class CategoriaBase(SQLModel):
    nombre: str

class Categoria(CategoriaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    productos: List["Producto"] = Relationship(back_populates="categoria")

class CategoriaRead(CategoriaBase):
    id: int

class ProductoBase(SQLModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: int
    stock: int
    categoria_id: int = Field(foreign_key="categoria.id")

class Producto(ProductoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    categoria: Optional[Categoria] = Relationship(back_populates="productos")

class ProductoCreate(ProductoBase):
    pass

class ProductoRead(ProductoBase):
    id: int
    categoria: Optional[CategoriaRead]

SQLModel.update_forward_refs()
