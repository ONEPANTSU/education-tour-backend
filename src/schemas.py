from typing import Optional

from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: Optional[str] = "success"
    message: Optional[str] = "Сообщение"
    data: Optional[dict] = None
    details: Optional[str] = "Детали"


class Response(BaseResponse):
    def __eq__(self, other: BaseResponse):
        if (
            (self.status == other.status or self.status is other.status)
            and (self.message == other.message or self.message is other.message)
            and (self.data == other.data or self.data is other.data)
            and (self.details == other.details or self.details is other.details)
        ):
            return True
        else:
            return False
