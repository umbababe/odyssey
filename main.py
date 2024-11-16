from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def read_root():
    return {"message": "Welcome to FastAPI on Debian 12!"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}
