import uvicorn
from fastapi import FastAPI

app = FastAPI()

dummy = "Testing"


@app.get("/")
def read_root():
    return {"Hello": "World"}
    print("Hello")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/async/")
async def async_read_root():
    return {"Hello": "World"}


@app.get("/async/items/{item_id}")
async def async_read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
