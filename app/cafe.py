from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Vaccination required to enter the cafe")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine is expired. Need to renew it.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("A mask is required to enter the cafe")
        return f"Welcome to {self.name}"
