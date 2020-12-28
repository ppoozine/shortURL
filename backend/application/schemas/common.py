from pydantic import BaseModel
from typing import List, Optional

class SuccessCreate(BaseModel):
    status: str = "Successfully Created!"