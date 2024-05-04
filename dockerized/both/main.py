# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() -> dict:
    """Reads the root path and returns a dictionary"""
    return {"Hello": "World...... fastapi"}