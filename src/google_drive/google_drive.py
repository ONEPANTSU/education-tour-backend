import os

from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from src.google_drive.directories import Directory, directory_id
from src.schemas import Response
from src.utils import Status, return_json


class Driver:
    def __init__(self) -> None:
        self.google_auth: GoogleAuth = GoogleAuth()
        self.google_auth.LocalWebserverAuth()

    def upload_file(
        self, filename: str, directory: Directory, temp_directory: str = "temp"
    ) -> Response:
        try:
            drive = GoogleDrive(self.google_auth)
            image = drive.CreateFile(
                {
                    "title": filename,
                    "parents": [
                        {"kind": "drive#fileLink", "id": directory_id[directory]}
                    ],
                }
            )
            image.SetContentFile(filename=os.path.join(temp_directory, filename))
            image.Upload()

            # file_link = f"https://drive.google.com/file/d/{image['id']}/view"

            file_link = f"https://drive.google.com/uc?export=view&id={image['id']}"

            return return_json(
                status=Status.SUCCESS,
                data={"file_link": file_link, "file_id": image["id"]},
            )
        except Exception as _ex:
            return return_json(status=Status.ERROR, details=str(_ex))

    def delete_file(self, filename: str, directory: Directory) -> Response:
        try:
            drive = GoogleDrive(self.google_auth)
            file_list = drive.ListFile(
                {"q": f"'{directory_id[directory]}' in parents and trashed=false"}
            ).GetList()

            for file in file_list:
                if file["title"] == filename:
                    file.Delete()
                    return return_json(status=Status.SUCCESS)

            return return_json(status=Status.ERROR, details="400 File not found")

        except Exception as _ex:
            return return_json(status=Status.ERROR, details=str(_ex))

    def delete_file_by_id(self, file_id: str, directory: Directory) -> Response:
        try:
            drive = GoogleDrive(self.google_auth)
            file_list = drive.ListFile(
                {"q": f"'{directory_id[directory]}' in parents and trashed=false"}
            ).GetList()

            for file in file_list:
                if file["id"] == file_id:
                    file.Delete()
                    return return_json(status=Status.SUCCESS)

            return return_json(status=Status.ERROR, details="400 File not found")

        except Exception as _ex:
            return return_json(status=Status.ERROR, details=str(_ex))
