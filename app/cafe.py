from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict | list) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        vac = visitor["vaccine"]
        if "expiration_date" not in vac:
            raise OutdatedVaccineError("Invalid vaccine info")
        exp = vac["expiration_date"]
        if exp < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing mask")
        return f"Welcome to {self.name}"
