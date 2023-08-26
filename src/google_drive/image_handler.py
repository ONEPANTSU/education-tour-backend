import os
from shutil import copyfileobj

from fastapi import UploadFile

from src.google_drive.directories import Directory
from src.google_drive.google_drive import Driver
from src.schemas import Response


class ImageHandler:
    def __init__(self):
        self.driver = Driver()

    def upload_image(self, image: UploadFile, directory: Directory) -> Response:
        with open("temp/" + image.filename, "wb") as file:
            copyfileobj(image.file, file)
        result = self.driver.upload_file(filename=image.filename, directory=directory)
        os.remove("temp/" + image.filename)
        return result

    def delete_image_by_id(self, image_id: str, directory: Directory) -> Response:
        return self.driver.delete_file_by_id(file_id=image_id, directory=directory)

    def delete_image_by_name(self, image_name: str, directory: Directory) -> Response:
        return self.driver.delete_file(filename=image_name, directory=directory)
