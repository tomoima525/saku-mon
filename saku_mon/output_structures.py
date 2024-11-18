from pydantic import BaseModel
from typing import List

class CodingTestIdea(BaseModel):
    ideas: List[str]