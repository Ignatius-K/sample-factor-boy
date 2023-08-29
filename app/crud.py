from app.db.models import Brand, Vehicle
from app.model_classes import Vehicle as VehicleModel, Brand as BrandModel
from app.db.db_conn import Session


session = Session()


def create_vehicle(vehicle: VehicleModel):

    session.add(Vehicle(
        name=vehicle.name,
        brand_id=vehicle.brand_id
    ))

    session.commit()


def create_brand(brand: BrandModel):

    session.add(Brand(
        name=brand.name
    ))

    session.commit()


__all__ = [
    'create_brand',
    'create_vehicle'
]