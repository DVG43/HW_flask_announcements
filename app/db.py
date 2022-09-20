from config import PG_DSN
from sqlalchemy.orm import sessionmaker
from models import Base
from sqlalchemy import (create_engine)

engine = create_engine(PG_DSN)  # дключение к базе.
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)




