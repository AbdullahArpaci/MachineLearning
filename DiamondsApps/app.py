import pickle
import pandas as pd
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI,Request
from pydantic import BaseModel

app = FastAPI()


templates = Jinja2Templates(directory="templetes")

with open("10-diamonds", "rb") as f:
    saved_file = pickle.load(f)
    model = saved_file["model"]
    encoders = saved_file["encoder"]
    scaler = saved_file["scaler"]


class DiamondFeatures(BaseModel):
    carat: float
    cut: str
    color: str
    clarity: str
    depth: float
    table: float
    x: float
    y: float
    z: float


@app.post("/predict")
async def predict(request: DiamondFeatures):
    input_frame = pd.DataFrame([request.model_dump()])
    for col in ["cut", "color", "clarity"]:
        encoder = encoders[col]
        input_frame[col] = encoder.transform(input_frame[col])

    input_scaled = scaler.transform(input_frame)


    y_pred = model.predict(input_scaled)

    return {"predicted_price": float(y_pred[0])}

@app.get("/",response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})