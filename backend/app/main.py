from fastapi import FastAPI

from app.routes import (
    health,
    upload,
    extract,
    reconcile,
    patch,
)

app = FastAPI(
    title="Compliance Evolution Engine API",
    description="AI-powered regulatory compliance intelligence platform.",
    version="0.1.0"
)

app.include_router(health.router)
app.include_router(upload.router)
app.include_router(extract.router)
app.include_router(reconcile.router)
app.include_router(patch.router)


@app.get("/")
def root():
    return {
        "project": "Compliance Evolution Engine",
        "status": "Running",
        "version": "0.1.0"
    }