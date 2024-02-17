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
            raise NotVaccinatedError("There is no vaccination.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccination period has expired.")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                "It is necessary to wear a protective mask."
            )
        return f"Welcome to {self.name}"
