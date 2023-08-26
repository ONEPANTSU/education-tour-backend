from fastapi import APIRouter, UploadFile

from src.google_drive.directories import Directory
from src.instruments import image_handler

image_router = APIRouter(prefix="/image", tags=["image"])


@image_router.post("/upload")
def upload_image(image: UploadFile, directory: Directory):
    return image_handler.upload_image(image=image, directory=directory)


@image_router.delete("/delete_by_id")
def delete_image_by_id(image_id: str, directory: Directory):
    return image_handler.delete_image_by_id(image_id=image_id, directory=directory)
