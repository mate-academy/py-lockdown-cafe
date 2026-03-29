import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Wow, {visitor['name']} is so late (cafe.py, line 16)."
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"Sorry, {visitor['name']}, you need "
                f"an update (cafe.py, line 21)."
            )
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                "I can see your face and I don`t like it (cafe.py, line 25)."
            )
        return f"Welcome to {self.name}"
