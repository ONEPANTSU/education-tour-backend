from fastapi import FastAPI

from src.event.router import category_router, event_router

app = FastAPI(title="Education Tourism")

app.include_router(event_router)
app.include_router(category_router)
