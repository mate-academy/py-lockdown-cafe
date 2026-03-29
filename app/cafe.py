from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine", 0):
            raise NotVaccinatedError("Visitor must be vaccinated")
        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("Vaccination is outdated")
        if not visitor.get("wearing_a_mask", 0):
            raise NotWearingMaskError("Visitor not wearing the mask")
        return f"Welcome to {self.name}"

    def __str__(self):
        return self.name
