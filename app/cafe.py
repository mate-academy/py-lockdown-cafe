import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor must be vaccinated to enter cafe."
            )

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                "Visitor vaccine has expired and is no longer valid."
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "Visitor must wear a mask to enter cafe."
            )

        return f"Welcome to {self.name}"
