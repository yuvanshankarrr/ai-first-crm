from fastapi import FastAPI

app =FastAPI(
    title="AI First CRM API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Welcome to AI First CRM API"
    }