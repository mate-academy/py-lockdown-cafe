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
            raise NotVaccinatedError("All visitors must be vaccinated!!!")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine outdated!!!")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitors must wear masks!!!")
        return f"Welcome to {self.name}"
