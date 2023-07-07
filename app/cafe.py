import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str:

        if not visitor.get("vaccine", None):
            raise NotVaccinatedError(
                "The visitor must be vaccinated"
            )

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "The vaccine has expired"
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "Visitor must have a mask"
            )

        return f"Welcome to {self.name}"
