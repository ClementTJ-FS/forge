"""FastAPI application for Forge."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class HealthResponse(BaseModel):
    """Pydantic model for /health response."""

    status: str


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Health check endpoint to verify if the backend server is running."""
    return HealthResponse(status="healthy")
