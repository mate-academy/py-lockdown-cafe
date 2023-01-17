import datetime
from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(" Vaccine is outdated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("The visitor has no mask")
        return f"Welcome to {self.name}"
