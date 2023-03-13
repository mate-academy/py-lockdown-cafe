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
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                "You are not vaccinated!"
            )
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                "Your vaccination period is overdue!"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "Please wear or buy a mask!"
            )
        return f"Welcome to {self.name}"
