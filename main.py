from fastapi import FastAPI
from app.schedules import Schedules
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000",  # Add any additional allowed origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"Hello": "V1"}

@app.get("/schedules")
def schedule():
    return Schedules([[False]*672,[True]*672]).compareMonday()

@app.post("/lists/")
async def process_lists(lists: List[List[int]]):
    return {"lists": lists}