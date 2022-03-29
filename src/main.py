from fastapi import FastAPI
from handler import handle_url
from predict import predict_model

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/predict_url")
async def predict_url(url: str):
    model_input = handle_url(url)
    model_output = predict_model(model_input)
    return model_output
