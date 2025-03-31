from fastapi import FastAPI , Depends ,HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
import schemas
import models
# from models import  User 

from database import Base , engine , SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



app = FastAPI()

@app.get("/")
def getall_User(db: Session = Depends(get_db)):
    users = db.execute(select(models.User)).scalars().all()
    return users

@app.post("/addUser")
def add_user(user: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(id=user.id, name=user.name, email=user.email,password = user.password)  
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/users/{id}", response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.execute(select(models.User).where(models.User.id == id)).scalar()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{id}", response_model=schemas.User)
def update_user(id: int, updated_user: schemas.User, db: Session = Depends(get_db)):
    user = db.execute(select(models.User).where(models.User.id == id)).scalar()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = updated_user.name
    user.email = updated_user.email
    user.password = updated_user.password
    db.commit()
    db.refresh(user)   
    return user

@app.delete("/users/{id}", status_code=204) 
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.execute(select(models.User).where(models.User.id == id)).scalar()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()





















# @app.get("/{id}")
# def getItem(id: int):
#     if id in fakedatabase:
#         return fakedatabase[id]
    
# @app.get("/{id}")
# def getItem(id:int,session: Session = Depends(get_session)):
#     User = session.query(models.User).get(id)
#     return User

# @app.post("/{id}")
# def addItem(User:schemas.User, session: Session = Depends(get_session)):
#     User = models.User(id=User.id)
#     # User = models.User(name=User.name)
#     # User = models.User(email=User.email)
#     # User = models.User(password=User.password)
#     session.add(User)
#     session.commit()
#     session.refresh(User)
#     return User


# @app.delete("/{id}")
# def deleteItem(id:int,session: Session = Depends(get_session)):
#     itemObject = session.query(models.User).get(id)
#     session.delete(itemObject)
#     session.commit()
#     return {"message":"Item deleted"}