from fastapi import FastAPI
from app.schedules import Schedules
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/schedules")
def schedule():
    return Schedules([[False]*672,[True]*672]).compareMonday()