
# main.py

# web framework for building APIs with Python
from fastapi import FastAPI
# local tunneling service for exposing local servers to the internet 

# environment variable dotenv
from dotenv import load_dotenv
import os

load_dotenv()

# web framework for building APIs with Python
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    
