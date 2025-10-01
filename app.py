import pickle 
from fastapi import FastAPI 
from pydantic import BaseModel 
import io
import requests
from fastapi.middleware.cors import CORSMiddleware
URL = "https://drive.google.com/uc?export=download&id=1M0Zat9TPqjoWb8MWEPGe5Fi0AceXUUNB"
response = requests.get(URL)
model = pickle.load(io.BytesIO(response.content))

class TextInput(BaseModel): 
    text: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict_sentiment(data: TextInput):
    try:
        prediction = model.predict([data.text])
        sentiment = prediction[0]
        return {"text": data.text, "sentiment": str(sentiment)}
    except Exception as e:
        # 👇 This will show the real cause of error in Swagger UI
        return {"error": str(e)}


