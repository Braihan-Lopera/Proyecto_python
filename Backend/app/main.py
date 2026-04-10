from fastapi import FastAPI
from app.entrypoints.http.client_routes import router as client_router
app = FastAPI()
app.include_router(client_router)
@app.get("/")
def root():
    return {"response": "Back is running :D"}