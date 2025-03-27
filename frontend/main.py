from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import requests

app = FastAPI()

# Set up the HTML template directory
templates = Jinja2Templates(directory="templates")

# Backend API URL 
BACKEND_URL = "http://backend:9567"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# get button
@app.post("/get_document/")
async def get_document():
    response = requests.get(f"{BACKEND_URL}/get_best_document")
    return response.json()

# insert button
@app.post("/insert_document/")
async def insert_document():
    response = requests.post(f"{BACKEND_URL}/insert_large_document")
    return response.json()
