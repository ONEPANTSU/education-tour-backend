import time

from fastapi import FastAPI, Request
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from src.config import ALLOWED_HOSTS, ORIGINS
from src.event_module.router import category_router, event_router, tag_router
from src.google_drive.router import image_router
from src.tour_module.router import tour_router
from src.university_module.router import university_router
from src.user_module.router import user_router
from src.utils import access_denied

app = FastAPI(title="Education Tourism")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)

ROUTERS_V1 = [
    event_router,
    category_router,
    tag_router,
    tour_router,
    university_router,
    user_router,
    image_router,
]

for router in ROUTERS_V1:
    app.include_router(router, prefix="/api/v1")


# @app.middleware("http")
# async def add_allow_hosts(request: Request, call_next):
#     ip = str(request.client.host)
#     if ip not in ALLOWED_HOSTS:
#         return JSONResponse(
#             status_code=status.HTTP_403_FORBIDDEN, content=access_denied().dict()
#         )
#     else:
#         response = await call_next(request)
#         return response
