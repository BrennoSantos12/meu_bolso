from fastapi import FastAPI 
from app.routers import users, categories, transactions

app = FastAPI()


app.include_router(users.router)
app.include_router(categories.router)
app.include_router(transactions.router)
