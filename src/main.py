from src.model import model_pipeline
from fastapi import FastAPI, UploadFile

from typing import Union

from fastapi import FastAPI
from PIL import Image
import io

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    image = Image.open(io.BytesIO(content))
    # image = Image(image.file)

    result = model_pipeline(text, image)
    return {"answer": result}