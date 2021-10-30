from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

meta_data = MetaData()
Base = declarative_base(metadata=meta_data)