from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    user_id: int

class CategoryResponse(BaseModel):
    id: int
    name: str
    user_id: int

    class config:
        from_attributes = True

class CategoryUpdate(BaseModel):
        name: str
        user_id: int
