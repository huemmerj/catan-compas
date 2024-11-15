# api/router.py
from fastapi import APIRouter

from api.endpoints import solver

# Create the main router
api_router = APIRouter()

# Include all endpoint routers with their prefixes and tags
api_router.include_router(solver.router, prefix="/solver", tags=["solver"])
