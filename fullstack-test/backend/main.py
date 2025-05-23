from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import json
from pathlib import Path
import os

app = FastAPI(title="Fullstack Test API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://frontend:5173", "*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# User data model
class User(BaseModel):
    first_name: str
    last_name: str

# File path for storing user data
DATA_FILE = Path("user_data.json")

def ensure_data_file():
    """Ensure the data file exists and is properly initialized"""
    if not DATA_FILE.exists():
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
    elif DATA_FILE.stat().st_size == 0:
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

def read_users():
    """Read users from the JSON file with error handling"""
    try:
        ensure_data_file()
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If file is corrupted, reset it
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
        return []
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading user data: {str(e)}")

def write_users(users):
    """Write users to the JSON file with error handling"""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(users, f, indent=2)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error writing user data: {str(e)}")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Fullstack Test API"}

@app.post("/users", response_model=User)
async def create_user(user: User):
    try:
        users = read_users()
        users.append(user.dict())
        write_users(users)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users", response_model=List[User])
async def get_users():
    try:
        return read_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Ensure the data file exists when starting the server
    ensure_data_file()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 