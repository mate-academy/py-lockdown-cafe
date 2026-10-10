from datetime import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if visitor["vaccine"]["expiration_date"] < datetime.today().date():
            raise OutdatedVaccineError(
                "The vaccine's expiration date has passed."
            )
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("The visitor does not have a mask.")
        return f"Welcome to {self.name}"
