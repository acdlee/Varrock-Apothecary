from fastapi import FastAPI
import sqlite3
from app.database import DB

app = FastAPI()
db = DB()

@app.get('/')
def index():
    return {"welcome": "to the apoth"}

@app.get('/herbs')
def read_herbs():
    global db
    return db.fetch_all_rows('herbs')

@app.get('/ingredients')
def read_ingredients():
    global db
    return db.fetch_all_rows('ingredients')

@app.get('/potions')
def read_potions():
    global db
    return db.fetch_all_rows('potions')