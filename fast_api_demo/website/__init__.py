from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import site

app = FastAPI()

app.mount("/static", StaticFiles(directory='./website/static'), name="static")
templates = Jinja2Templates(directory="./website/templates")

from website.routes import main