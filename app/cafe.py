from datetime import date
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        today = date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        elif today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("All friends should be vaccinated")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Error")
        else:
            return f"Welcome to {self.name}"
