# 🚀 Smart ML Prediction API (FastAPI + PostgreSQL)

This project is a complete end-to-end Machine Learning system that serves predictions through a REST API built with FastAPI and stores results in PostgreSQL.

---

##  Project Overview

This system:
- Trains a Machine Learning model
- Serves predictions via FastAPI
- Stores predictions in PostgreSQL
- Returns real-time responses through API

---

##  Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Scikit-learn
- Pandas
- Joblib
- Uvicorn

---

##  Features

- ✔ ML model training pipeline
- ✔ `/predict` endpoint
- ✔ PostgreSQL integration
- ✔ Data validation with Pydantic
- ✔ Persistent prediction storage
- ✔ RESTful API design

---

##  Machine Learning Model

The model predicts house prices based on:

- Area
- Number of bedrooms
- Location 

Trained using Scikit-learn and saved with Joblib.

---
## How to Run
-Install dependencies:

 pip install -r requirements.txt
-Start PostgreSQL
 Make sure database is running locally.
-Run server
 uvicorn main:app --reload
-Open API docs
 http://127.0.0.1:8000/docs

##  API Endpoints

### POST /predict

Request:
```json
{
  "area": 100,
  "bedrooms": 3,
  "location": "new york"
}

Response:
{
  "id": 1,
  "area": 100,
  "bedrooms": 3,
  "location": "new york",
  "prediction": 255555.55
}


 
