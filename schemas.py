from pydantic import BaseModel

class PredictionCreate(BaseModel):
    area: float
    bedrooms: int
    location: str

class PredictionResponse(BaseModel):
    id: int
    area: float
    bedrooms: int
    location: str
    prediction: float

    class Config:
        orm_mode = True