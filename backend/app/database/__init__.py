from app.database.connection import Base, engine

# Import all models so SQLAlchemy knows about them
from app.models.hcp import HCP
from app.models.interaction import Interaction

Base.metadata.create_all(bind=engine)