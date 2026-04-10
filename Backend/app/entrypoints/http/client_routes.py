from fastapi import APIRouter
from app.infraestructure.json.json_client_repository import JsonClientRepository
from app.domain.models.cliente import Client
from app.application.useCases.create_client import createClientUseCase


router = APIRouter()

@router.post("/clients")
def create_client(data:dict):

    client = Client(id= data["id"], name = data["name"], email = data["email"] )
    repository = JsonClientRepository()
    use_case = createClientUseCase(repository)
    use_case.execute(client)
    return {"Message": "Cliente guardado"}