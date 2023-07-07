import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str:

        if visitor.get("vaccine") is None:
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
