from website import app, templates
from fastapi import Request


@app.get("/")
def home(request:Request):
  return {"message":"Hello world"}