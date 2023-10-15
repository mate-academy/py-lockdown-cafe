import datetime
from app.errors import *


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s"
                                       f" vaccine is expired!")
        if not visitor.get("wearing_a_mask") or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor['name']}"
                                      f" is not wearing a mask!")
        return f"Welcome to {self.name}"
