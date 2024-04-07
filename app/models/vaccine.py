from datetime import date
from typing import TypedDict


class Vaccine(TypedDict):
    expiration_date: date
    name: str
