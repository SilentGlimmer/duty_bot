from fastapi import FastAPI
from fastapi_pagination import add_pagination

from duty.api.routers import router as api_router

app = FastAPI()
app.include_router(api_router)

add_pagination(app)
