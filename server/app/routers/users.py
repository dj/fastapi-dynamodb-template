from fastapi import APIRouter
from datetime import timedelta
from typing import Annotated, Any

from fastapi import Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY

from ..settings import AppSettings
from ..schemas.users import UserPost, User
from ..schemas.token import Token
from ..auth import (
    get_current_user,
    authenticate_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
)
from ..db.users import insert_user, UserAlreadyExists

router = APIRouter()


@router.post("/users", status_code=HTTP_201_CREATED)
def create_user(
    data: UserPost,
    response: Response,
):
    try:
        resp = insert_user(data)
        return resp
    except UserAlreadyExists:
        response.status_code = HTTP_422_UNPROCESSABLE_ENTITY
        return {"error": "username or email already exists"}


@router.get("/users/me")
async def read_current_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.get("/users/me/items/")
async def read_current_users_items(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], settings: AppSettings
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        secret_key=settings.secret_key,
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}
