from enum import Enum

from loguru import logger

from src.schemas import Response


class Status(Enum):
    SUCCESS = "200 Success"
    ERROR = "400 Error"
    ACCESS_ERROR = "403 Access Denied"


def return_json(
    status: Status = Status.ERROR,
    message: str = None,
    data: dict = None,
    details: str = None,
) -> Response:
    return Response(status=status.value, message=message, data=data, details=details)


def access_denied() -> Response:
    return Response(
        status=Status.ACCESS_ERROR.value,
        message="Произошла ошибка при попытке запроса",
        details="Отказано в правах",
    )


logger.add(
    "education_tour.log",
    format="{time}\t|\t{level}\t|\t{message}",
    level="INFO",
    rotation="10MB",
    compression="zip",
)


class Role(Enum):
    GUEST = "GUEST"
    USER = "USER"
    UNIVERSITY = "UNIVERSITY"
    ADMIN = "ADMIN"


role_access = {
    Role.GUEST: 0,
    Role.USER: 1,
    Role.UNIVERSITY: 2,
    Role.ADMIN: 3,
}
