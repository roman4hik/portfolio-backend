from enum import Enum


class Roles(Enum):
    ADMIN = "admin"
    AUTHOR = "user"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
