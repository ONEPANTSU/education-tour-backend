from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.event_module.router import category_router, event_router, tag_router
from src.tour_module.router import tour_router
from src.university_module.router import university_router
from src.user_module.router import user_router

app = FastAPI(title="Education Tourism")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ROUTERS = [
    event_router,
    category_router,
    tag_router,
    tour_router,
    university_router,
    user_router,
]

for router in ROUTERS:
    app.include_router(router)
