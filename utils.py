from models import produtos

def procurar_por_id(id):
    return next((p for p in produtos if p["id"] == id), None)