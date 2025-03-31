from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy_database_URL ="postgresql://postgres:Santra%40213@localhost:5432/Storage"
engine = create_engine("postgresql://postgres:Santra%40213@localhost:5432/Storage",echo=True)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


Base = declarative_base()


