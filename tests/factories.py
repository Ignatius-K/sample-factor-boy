# main
import factory

# local
from app.db.db_conn import Session
from app.db.models import Brand, Vehicle


class BrandFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Brand
        sqlalchemy_session = Session()
    
    name = factory.Faker('name')


class VehicleFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Vehicle
        sqlalchemy_session = Session
    
    name = factory.Faker("name")
    brand_id = factory.Sequence(lambda n: n)
    