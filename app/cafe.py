from datetime import date
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor['name']
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{name} should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{name}, your vaccination is outdated ;(")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{name}, you are obliged to wear a mask")
        return f"Welcome to {self.name}"
