from fastapi import FastAPI
from db import engine
from router import brand
import models

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(brand.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
