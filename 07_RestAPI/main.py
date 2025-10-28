from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI() #später router = APIRouter()

## Schema Definition für Items
class Item(BaseModel):
    name:str
    price:float
    description:str | None = None


############# Routes / Endpoint #########
@app.get("/") # http://127.0.0.1:8000/
def get_root():
    return {"message":"Hallo Rest"}

@app.get("/items/{item_id}") #http://127.0.0.1:8000/items/12?q=hallo
def get_item(item_id:int, q:str):
    return {"item_id":item_id,"query":q}



@app.post("/items")
def creat_item(item:Item):
    return {"message":"Item erhalten","item":item}


## put/delete