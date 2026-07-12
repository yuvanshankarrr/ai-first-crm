from app.database.connection import Base, engine

from app.models.hcp import HCP
from app.models.interaction import Interaction


# Import all models
from app.models.hcp import HCP

Base.metadata.create_all(bind=engine)

print(" Database Tables Created Successfully!")
