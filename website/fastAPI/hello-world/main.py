# go to docs at http://127.0.0.1:8000/docs
# run with uvicorn main:app --reload
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []

@app.get("/") # Decorator
def root():
    return {"Hello": "World"}

# Routes :

# Example usage:
# curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=foo'
@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

# curl -X POST -H "Content-Type: application/json" -d {"text":"here", "is_done":true"} 'http://127.0.0.1:8000/items2'

# curl -X POST -H "Content-Type: application/json" -d {"text":"appple"} 'http://127.0.0.1:8000/items2?items'
@app.post("/items2")
def create_item(item: Item):
    items.append(item)
    return items


# Example usage:
# curl -X GET -H "Content-Type: application/json" 'http://127.0.0.1:8000/items'
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]


# curl -X GET -H "Content-Type: application/json" 'http://127.0.0.1:8000/items/0'
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

