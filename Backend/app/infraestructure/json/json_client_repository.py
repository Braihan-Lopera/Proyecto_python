import os
import json
from app.domain.models.cliente import Client
from app.domain.repositories.client_repository import ClientRepository


class JsonClientRepository(ClientRepository):
    def save(self, client: Client) -> None:
        file_path = "cliente.json"

        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([], file)

        with open(file_path, "r") as file:
            content = file.read()

        if content.strip():
            clients = json.loads(content)
        else:
            clients = []

        clients.append(
            {
                "id": len(clients) + 1,
                "name": client.name,
                "email": client.email
            }
        )

        with open(file_path, "w") as file:
            json.dump(clients, file, indent=4)

    def get(self, client_id: int) -> Client | None:
        file_path = "cliente.json"

        if not os.path.exists(file_path):
            return None

        with open(file_path, "r") as file:
            content = file.read()

        if not content.strip():
            return None

        clients = json.loads(content)

        for c in clients:
            if c["id"] == client_id:
                return Client(
                    id=c["id"],
                    name=c["name"],
                    email=c["email"]
                )

        return None

    def delete(self, client_id: int) -> None:
        file_path = "cliente.json"

        if not os.path.exists(file_path):
            return

        with open(file_path, "r") as file:
            content = file.read()

        if not content.strip():
            return

        clients = json.loads(content)
        clients = [c for c in clients if c["id"] != client_id]

        with open(file_path, "w") as file:
            json.dump(clients, file, indent=4)

    def update(self, client: Client) -> None:
        file_path = "cliente.json"

        if not os.path.exists(file_path):
            return

        with open(file_path, "r") as file:
            content = file.read()

        if not content.strip():
            return

        clients = json.loads(content)

        for index, stored_client in enumerate(clients):
            if stored_client["id"] == client.id:
                clients[index] = {
                    "id": client.id,
                    "name": client.name,
                    "email": client.email
                }
                break

        with open(file_path, "w") as file:
            json.dump(clients, file, indent=4)