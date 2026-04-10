from abc import ABC, abstractmethod
from app.domain.models.cliente import Client

class ClientRepository(ABC):
    @abstractmethod
    def save(self, client:Client) -> None:
        pass
    
    @abstractmethod
    def update(self, client:Client) -> None:
        pass

    @abstractmethod
    def get(self, client_id:str) -> Client:
        pass
    
    @abstractmethod
    def delete(self, client_id:str) -> None:
        pass