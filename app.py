from cnnClassifier.utils.common import decode_image
from cnnClassifier.pipeline.stage05_Predict import PredictionPipeline
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/train")
async def train_route():
    import subprocess
    subprocess.run(["python", "main.py"])
    return {"message": "Training done successfully!"}


@app.post("/predict")
async def predict_route(image: dict):
    try:
        clApp = ClientApp()
        decode_image(image["image"], clApp.filename)
        result = clApp.classifier.predict()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)
