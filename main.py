from fastapi import FastAPI
from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends

from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

# routers: comentar hasta que los crees
from routers import todos

import config

app = FastAPI()

# routers: comentar hasta que los crees
app.include_router(todos.router)

# Lista de orígenes permitidos para CORS
origins = [
    "http://localhost:3000",
    "https://frontend-netxjs-versel-dm-jnfn.vercel.app",
]

# Configuración de CORS para permitir solicitudes desde los orígenes específicos
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Usar la lista de orígenes definidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Manejador global de excepciones HTTP


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# Uso de configuración de la aplicación con lru_cache


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    # Imprimir la configuración app_name
    print(settings.app_name)
    return "Hello World"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
