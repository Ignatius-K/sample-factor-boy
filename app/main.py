from fastapi import FastAPI
from app.model_classes import Vehicle, Brand
from app.crud import create_vehicle, create_brand

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Hello world"}


@app.post('/app/add-vehicle')
def add_vehicle(vehicle: Vehicle):
    create_vehicle(vehicle)


@app.post('/app/add-brand')
def add_brand(brand: Brand):
    create_brand(brand)
