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

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None:
            raise OutdatedVaccineError("Vaccine expiration date is missing.")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"Vaccine expired on"
                                       f" {expiration_date}.")

        if "wearing_a_mask" not in visitor:
            raise NotWearingMaskError("Visitor need to wear mask")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor need to wear mask")

        return f"Welcome to {self.name}"
