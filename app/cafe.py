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
            raise NotVaccinatedError("Visitor is not vaccinated.")
        elif not isinstance(
                visitor["vaccine"].get("expiration_date"),
                datetime.date
        ):
            raise OutdatedVaccineError(
                "Vaccine expiration date is not a valid date."
            )
        elif visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired.")
        elif visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
