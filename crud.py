from sqlalchemy.orm import Session
import models

def create_prediction(db: Session, data, pred_value):
    db_obj = models.Prediction(
        area=data.area,
        bedrooms=data.bedrooms,
        location=data.location,
        prediction=pred_value
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_predictions(db: Session):
    return db.query(models.Prediction).all()