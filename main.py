from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from db import engine, SessionLocal
import joblib

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Load model ONCE
model = joblib.load("ml/model.pkl")

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/predict", response_model=schemas.PredictionResponse)
def predict(data: schemas.PredictionCreate, db: Session = Depends(get_db)):
    try:
        features = [[data.area, data.bedrooms]]
        pred = float(model.predict(features)[0])

        db_obj = crud.create_prediction(db, data, pred)
        return db_obj

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/history", response_model=list[schemas.PredictionResponse])
def get_history(db: Session = Depends(get_db)):
    return crud.get_predictions(db)