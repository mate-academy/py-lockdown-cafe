from datetime import date
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All visitors must be vaccinated")
        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Vaccine expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear a mask")
        return f"Welcome to {self.name}"
