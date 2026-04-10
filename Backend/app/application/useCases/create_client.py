from app.domain.models.cliente import Client
from app.domain.repositories.client_repository import ClientRepository

class createClientUseCase:
    def __init__(self, client_repository:ClientRepository):
        self.client_repository = client_repository
    
    def execute(self,client:Client) -> None:
        self.client_repository.save(client)