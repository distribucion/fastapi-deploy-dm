# from fastapi import FastAPI, Depends
# from functools import lru_cache
# from typing import Union
# from fastapi.responses import PlainTextResponse
# from starlette.exceptions import HTTPException as StarletteHTTPException
# from fastapi.middleware.cors import CORSMiddleware

# # Importa los routers solo si ya existen. Si no, comenta esta línea.
# # from routers import todos
# from routers import todos
# import config

# app = FastAPI()
# app.include_router(todos.router)

# # Incluye el router si ya existe. Si no, comenta esta línea.
# # app.include_router(todos.router)

# # Lista de orígenes permitidos para CORS
# # origins = [
# #     "http://localhost:3000",
# #     "https://frontend-netxjs-versel-dm-jnfn.vercel.app/",
# # ]

# # Configuración de CORS para permitir solicitudes desde los orígenes específicos
# app.add_middleware(
#     CORSMiddleware,
#     # Usar la lista de orígenes definidos
#     allow_origins=["https://frontend-netxjs-versel-dm-jnfn.vercel.app"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Manejador global de excepciones HTTP


# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     print(f"{repr(exc)}")
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# # Uso de configuración de la aplicación con lru_cache


# @lru_cache()
# def get_settings():
#     return config.Settings()


# @app.get("/")
# def read_root(settings: config.Settings = Depends(get_settings)):
#     # Imprimir la configuración app_name
#     print(settings.app_name)
#     return "Hello World"


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

from fastapi import FastAPI, Depends
from functools import lru_cache
from typing import Union
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

# routers: comment out next line till create them
from routers import todos

import config

app = FastAPI()

# router: comment out next line till create it
app.include_router(todos.router)


# origins = [
#     "http://localhost:3000",
#     "https://frontend-netxjs-versel-dm-jnfn.vercel.app/",
# ]

# # CORS configuration, needed for frontend development
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000",
#                    "https://frontend-netxjs-versel-dm-jnfn.vercel.app",],
#     allow_credentials=True,
#     allow_methods=["*"],
# #     allow_headers=["*"],
# )


origins = [
    # Cambia esto por el dominio de tu aplicación en Vercel
    "https://frontend-netxjs-versel-dm-jnfn.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# global http exception handler, to handle errors
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# to use the settings


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    # print the app_name configuration
    print(settings.app_name)
    return "Hello World"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
