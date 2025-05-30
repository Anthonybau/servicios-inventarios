from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_y_listar_categoria(client):
    # Crear
    resp = client.post("/categorias/", json={"nombre": "Test Categoría"})
    assert resp.status_code == 200
    categoria = resp.json()
    assert categoria["nombre"] == "Test Categoría"
    cat_id = categoria["id"]

    # Listar
    resp = client.get("/categorias/")
    data = resp.json()
    assert any(c["id"] == cat_id for c in data)

def test_crear_y_listar_producto(client):
    # Crear categoría primero
    resp = client.post("/categorias/", json={"nombre": "Electrónica"})
    categoria = resp.json()
    cat_id = categoria["id"]

    # Crear producto
    producto_payload = {
        "nombre": "Mouse Inalámbrico",
        "descripcion": "Con Bluetooth",
        "precio": 19990,
        "stock": 25,
        "categoria_id": cat_id
    }
    resp = client.post("/productos/", json=producto_payload)
    assert resp.status_code == 200
    producto = resp.json()
    assert producto["nombre"] == "Mouse Inalámbrico"

    # Listar productos
    resp = client.get("/productos/")
    productos = resp.json()
    assert any(p["nombre"] == "Mouse Inalámbrico" for p in productos)
