from pydantic import BaseModel
from typing import Optional, Any, List


class UserData(BaseModel):
    login: str
    password: str
    email: Optional[str] = None


class UpdateUser(BaseModel):
    pubkey: Optional[str] = None
    image_url: Optional[str] = None
    description: Optional[str] = None
    theme: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    badges: Optional[str] = None
    username: Optional[str] = None
    about: Optional[str] = None


class UpdateUserKeys(BaseModel):
    key_pair: List[dict]


class CreateGroup(BaseModel):
    owner: Optional[str] = None
    image_url: Optional[str] = None
    name: str
    key: str


class InviteUser(BaseModel):
    group_id: int
    message_text: str
    user_login: str
    key: str


class KickUser(BaseModel):
    group_id: int
    message_text: str
    user_id: int


class SetupKey(BaseModel):
    user_id: int
    key: str
    user_key: str


class MessageData(BaseModel):
    target: int
    message_text: str
    group: bool
    attachment: List[Any] = None


class DeleteMessage(BaseModel):
    group: bool
    message_id: int


class UpdateMessage(BaseModel):
    group: bool
    message_id: int
    text: str


class PostData(BaseModel):
    id: Optional[int] = None
    text: str
