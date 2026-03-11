from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from app.database import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse,
    TransactionUpdate,
)

router = APIRouter(prefix="/transactions", tags=["Transactions"])

DBSession = Annotated[Session, Depends(get_db)]


@router.get("/", response_model=list[TransactionResponse])
def get_transactions(db: DBSession):
    transactions = db.query(Transaction).all()
    return transactions


@router.post("/", response_model=TransactionResponse)
def create_transaction(
    transaction: TransactionCreate,
    db: DBSession
):
    new_transaction = Transaction(**transaction.model_dump())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return new_transaction


@router.put("/{transaction_id}", response_model=TransactionResponse)
def edit_transaction(
    transaction_id: int,
    transaction_data: TransactionUpdate,
    db: DBSession
):
    transaction = (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id)
        .first()
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Essa transação não existe."
        )

    update_data = transaction_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(transaction, field, value)

    db.commit()
    db.refresh(transaction)
    return transaction
