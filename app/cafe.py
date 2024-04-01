from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Man should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Human should be vaccinated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Man should buy mask")
        return f"Welcome to {self.name}"
