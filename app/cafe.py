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
                "NotVaccinatedError: please get vaccinated"
            )

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "OutdatedVaccineError: your vaccination period has expired"
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "NotWearingMaskError: please wear a mask"
            )

        return f"Welcome to {self.name}"
