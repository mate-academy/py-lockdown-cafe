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
            name = visitor.get("name", "Unknown visitor")
            raise NotVaccinatedError(
                f"{name} is not vaccinated."
            )

        expiration_date = visitor["vaccine"].get("expiration_date")
        if not expiration_date or expiration_date < datetime.date.today():
            name = visitor.get("name", "Unknown visitor")
            raise OutdatedVaccineError(
                f"{name}'s vaccine is expired or missing."
            )

        if not visitor.get("wearing_a_mask", False):
            name = visitor.get("name", "Unknown visitor")
            raise NotWearingMaskError(
                f"{name} is not wearing a mask."
            )

        return f"Welcome to {self.name}"
