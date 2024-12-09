from fastapi import FastAPI
from infra.api.routers import user_routes

app = FastAPI()

app.include_router(user_routes.router)