from pydantic import BaseModel


class Address(BaseModel):
    country: str = None
    city: str = None
    street: str = None
    house: int = None
    corps: int = None
    building: int = None
    level: int = None
    flat: int = None
    office: int = None
