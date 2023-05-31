from fastapi import FastAPI
from db import engine
import models

app = FastAPI()
# models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Hello World"}
