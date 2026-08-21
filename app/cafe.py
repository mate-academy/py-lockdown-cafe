import datetime

from app.errors import (
    OutdatedVaccineError,
    NotWearingMaskError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Person is not vaccinated")

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")

        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask")
        else:
            return f"Welcome to {self.name}"
