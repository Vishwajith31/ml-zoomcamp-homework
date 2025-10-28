import requests

url = "http://localhost:8000/predict"

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client)
result = response.json()

if response.status_code == 200:
    print(f"Conversion probability: {result['conversion_probability']:.3f}")
else:
    print(f"Error: {response.text}")    