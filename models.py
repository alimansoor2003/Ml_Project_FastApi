from sqlalchemy import Column, Integer, Float, String
from db import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    area = Column(Float)
    bedrooms = Column(Integer)
    location = Column(String)
    prediction = Column(Float)