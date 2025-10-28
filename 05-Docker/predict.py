import pickle

model_file = 'pipeline_v1.bin'
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)
    
customer = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}    

probability = model.predict_proba([customer])[0, 1]
print(f"Conversion probability: {probability:.3f}")