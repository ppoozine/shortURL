from pydantic import BaseModel
from typing import List, Optional

class UrlSchema(BaseModel):
    id: int
    old_url: str
    new_url: str

class RequestUrl(BaseModel):
    old_url: str

class ResponsesUrl(BaseModel):
    new_url: str