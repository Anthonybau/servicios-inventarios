from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import create_db_and_tables
from .routes import productos, categorias

app = FastAPI(title="Microservicio de Productos con Categorías")


# Orígenes permitidos (frontend en desarrollo, por ejemplo)
origins = [
    "http://localhost:5173",  # Vite
    "http://127.0.0.1:5173",  # Vite en otra forma
    # Agrega otros dominios si despliegas luego
]

# Configurar el middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir estos orígenes
    allow_credentials=True,
    allow_methods=["*"],     # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],     # Permitir todos los headers
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(productos.router)
app.include_router(categorias.router)
