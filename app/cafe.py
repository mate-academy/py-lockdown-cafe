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
        name = visitor["name"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{name} is not vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{name}'s vaccine is outdated")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{name} is not wearing mask")
        else:
            return f"Welcome to {self.name}"
