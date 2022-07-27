
from fastapi import FastAPI
from hotel.db.engine import init_db
from hotel.routers import customers, rooms, bookings
import sqlite3


app = FastAPI()
DB_FILE = "sqlite:///hotel.db"

@app.on_event("startup")
def startup_event():
    init_db(DB_FILE)

@app.get("/")
def read_root():
    return "Hey there, this is the GOAT api and the server is up and running"

app.include_router(rooms.router)
app.include_router(customers.router)
app.include_router(bookings.router)


