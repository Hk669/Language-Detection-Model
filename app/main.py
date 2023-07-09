from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline

app = FastAPI()

class TextIn(BaseModel):
    text : str

class PredictionOut(BaseModel):
    language : str

@app.get('/')
def home():
    return {"message": "Welcome to the language detection API!"}

@app.post("/predict",response_model = PredictionOut)
async def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {'language' : language}

'''if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host='127.0.0.1',port=5000)'''
