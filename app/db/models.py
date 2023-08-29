from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class Brand(Base):
    __tablename__ = 'Brand'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))

    def __repr__(self):
        return self.name


class Vehicle(Base):
    __tablename__ = 'Vehicle'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    brand_id = Column(Integer, ForeignKey("Brand.id"), nullable=False)

    def __repr__(self):
        return self.name
