from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    name: str

@app.get("/")
def root():
    return {"Hello": "World"}   

@app.post("/items/")
def create_item(item: Item):
    items.append(item.name)
    return {"item": item.name}
@app.get("/items/")
def read_items():
    return {"items": items} 
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < len(items):
        return {"item": items[item_id]}
    return {"error": "Item not found"}, 404     