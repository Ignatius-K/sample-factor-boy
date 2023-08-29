from pydantic import BaseModel

class Vehicle(BaseModel):
    name: str
    brand_id: int


class Brand(BaseModel):
    name: str