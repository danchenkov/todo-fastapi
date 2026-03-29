from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.todos import router as todos_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(todos_router)