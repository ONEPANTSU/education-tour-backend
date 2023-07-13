from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.event_module.router import category_router, event_router

app = FastAPI(title="Education Tourism")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(event_router)
app.include_router(category_router)
