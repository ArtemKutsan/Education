# Импорт диблиотек
from fastapi import FastAPI  # библиотека для работы FastAPI


# Первое приложение FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}