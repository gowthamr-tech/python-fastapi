from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD + PostgreSQL")


@app.get("/")
def health_check() -> dict[str, str]:
    return {"message": "FastAPI CRUD API is running"}


@app.post("/items", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.get("/items", response_model=list[schemas.ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)


@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db=db, item_id=item_id, item=item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    print(f"Attempting to delete item with ID: {item_id}")
    deleted = crud.delete_item(db=db, item_id=item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.post("/items/add", response_model=schemas.ItemResponse)
# def add_item(item:Json):



