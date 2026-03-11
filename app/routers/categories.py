from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from app.schemas.transaction import TransactionResponse


router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


@router.get("/", response_model=list[CategoryResponse])
def get_categores(db: Session = Depends(get_db)):
    categories =  db.query(Category).all()
    return categories
        

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    categories = db.query(Category).filter(Category.id == category_id).first()
   
    if not categories:
        raise HTTPException(status_code=404, detail="Essa categoria não existe.")
    return categories
    

@router.get("/transactions/{category_id}", response_model=list[TransactionResponse])
def get_category_transaction(category_id: int, db: Session = Depends(get_db)):
    categories = db.query(Category).filter(Category.id == category_id).first()
   
    if not categories:
        raise HTTPException(status_code=404, detail="Essa categoria não existe.")
    return categories.transactions


@router.put("/{category_id}", response_model=CategoryResponse)
def edit_category(category_id: int, category_data: CategoryUpdate, db: Session = Depends(get_db)):

    categories = db.query(Category).filter(Category.id == category_id).first()

    if not categories:
        raise HTTPException(status_code=404, detail="Essa categoria não existe.")

    update_data = category_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(categories, field, value)

    db.commit()
    db.refresh(categories)
    return categories
    
