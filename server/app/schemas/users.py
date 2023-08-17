from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str | None = None
    disabled: bool | None = None


class UserRecord(User):
    hashed_password: str


class UserPost(BaseModel):
    username: str
    email: str | None = None
    password: str | None = None
    bio: str = ""
