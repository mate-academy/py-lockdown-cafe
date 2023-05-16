from datetime import date
from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("All friends should be vaccinated")
        expiration_date = vaccine.get("expiration_date")
        if expiration_date and expiration_date < date.today():
            raise OutdatedVaccineError("All friends should be vaccinated")
        wearing_a_mask = visitor.get("wearing_a_mask")
        if not wearing_a_mask:
            raise NotWearingMaskError("Please, wear your mask")
        return f"Welcome to {self.name}"
