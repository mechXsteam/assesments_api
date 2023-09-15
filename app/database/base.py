from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

# Create a new instance of MetaData
metadata = MetaData()

# Create the Base object and associate it with the metadata
Base = declarative_base(metadata=metadata)
