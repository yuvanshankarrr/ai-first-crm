# import app.database.init_db
from app.database import init_db
from app.models.hcp import HCP
from app.models.interaction import Interaction
from fastapi import FastAPI
from app.api.hcp import router as hcp_router 
from app.api.interaction import router as interaction_router
from fastapi.middleware.cors import CORSMiddleware

import app.models

app =FastAPI(
    title="AI First CRM API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(hcp_router)
app.include_router(interaction_router)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Welcome to AI First CRM API"
    }