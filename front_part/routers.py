import os

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix='')
templates = Jinja2Templates(directory=os.path.dirname(os.path.abspath(__file__)))


@router.get("/", tags=['Frontend'], response_class=HTMLResponse)
async def frontend(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})
