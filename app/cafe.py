from datetime import date
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
                f"Visitor: {visitor['name']} "
                f"is not vaccinated."
            )

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor['name']} "
                f"your vaccine expiration date has expired"
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"Visitor {visitor['name']} is not wearing mask. "
                f"Cannot visit {self.name}."
            )
        return f"Welcome to {self.name}"
