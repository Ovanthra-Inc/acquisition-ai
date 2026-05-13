from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# To avoid circular imports, models should not be imported here.
