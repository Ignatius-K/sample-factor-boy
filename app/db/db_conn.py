# utils
import os
from dotenv import load_dotenv

# main
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# local
from app.db.models import Base

load_dotenv(verbose=True)
DB_URL = os.getenv('DB_URL')

engine = create_engine(
    url=DB_URL
)
    
Base.metadata.create_all(engine)

Session = sessionmaker(engine)



