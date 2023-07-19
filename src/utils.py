from enum import Enum

from loguru import logger

from src.schemas import Response


class Status(Enum):
    SUCCESS = "200 Success"
    ERROR = "400 Error"


def return_json(
    status: Status = Status.ERROR,
    message: str = None,
    data: dict = None,
    details: str = None,
) -> Response:
    return Response(status=status.value, message=message, data=data, details=details)


logger.add(
    "education_tour.log",
    format="{time}\t|\t{level}\t|\t{message}",
    level="INFO",
    rotation="10MB",
    compression="zip",
)
