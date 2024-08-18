# main.py
# in terminal: uvicorn main:app --reload

import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from db import DatabaseConnection


# Load environment variables
load_dotenv()

# Database connection details
DATABASE_URL = os.getenv("DATABASE_URL")
print('DATABASE_URL:', DATABASE_URL)

dbconn = DatabaseConnection()

# Database connection function
async def get_db_connection():
    conn = None
    try:
        conn = dbconn.get_session()
    except Exception as e:
        print("Failed to connect to the database", conn)
        print(e)
        raise HTTPException(status_code=500, detail="Failed to connect to the database")
    return conn


# Initialize FastAPI app
app = FastAPI()

# hello world api endpoint
@app.get("/")
async def read():
    # create a connection to the database
    conn = await get_db_connection()
    
    return {
        "Hello": "World - check for db connection",
        "Connection": conn
    }

