# utils
import os
from dotenv import load_dotenv

# main
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# local
from app.db.models import Base

load_dotenv()

TEST = bool(int(os.getenv('TEST')))
TEST_DB_URL = os.getenv('TEST_DB_URL')
DB_URL = os.getenv('DB_URL')

engine = create_engine(
    url= TEST_DB_URL if TEST else DB_URL
)
    
Base.metadata.create_all(engine)

Session = sessionmaker(engine)

__all__ = [
    'Session'
]

