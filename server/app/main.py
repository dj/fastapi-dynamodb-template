from typing import Annotated
from fastapi import FastAPI, Depends
from functools import lru_cache

from .routers import users


app = FastAPI()

app.include_router(users.router)
