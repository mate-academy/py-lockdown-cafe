import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("The cafe visitor is not vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccination date is overdue")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("A cafe visitor is not wearing a mask")

        return f"Welcome to {self.name}"
