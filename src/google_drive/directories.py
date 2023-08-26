from enum import Enum

from src.config import EVENT, ROOT, TOUR, UNIVERSITY, USER


class Directory(Enum):
    EVENT = "Event"
    TOUR = "Tour"
    UNIVERSITY = "University"
    USER = "User"
    ROOT = "ROOT"


directory_id = {
    Directory.EVENT: EVENT,
    Directory.TOUR: TOUR,
    Directory.UNIVERSITY: UNIVERSITY,
    Directory.USER: USER,
    Directory.ROOT: ROOT,
}
