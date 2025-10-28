import pickle
from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore

with open('/code/pipeline_v2.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)
    
app = FastAPI()

class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

@app.post("/predict")
def predict(lead: Lead):
    
    lead_dict = lead.model_dump()
    probability = pipeline.predict_proba(lead_dict)[0, 1]
    return {
        "conversion_probability": probability
    }
    
@app.get("/")
def read_root():
    return {"message": "Lead Scoring API is running!"}    