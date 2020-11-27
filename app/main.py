from fastapi import FastAPI
from .app import is_alive_host
from .status import Status


app = FastAPI()


@app.get('/')
def index():
    return {'title': 'Hello'}


@app.get('/healthz')
def wrapper_is_alive_host(hostname : str):
    status = Status.up if is_alive_host(hostname) else Status.down
    return {'status': status}

