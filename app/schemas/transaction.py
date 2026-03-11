from pydantic import BaseModel


class TransactionCreate(BaseModel):
    description: str
    amount: int 
    type: str
    user_id: int
    category_id: int 


class TransactionResponse(BaseModel):
        id: int
        description: str
        amount: int 
        type: str
        user_id: int
        category_id: int 
            
        class config:
           from_attributes = True

class TransactionUpdate(BaseModel):
        description: str
        amount: int 
        type: str
        category_id: int 


