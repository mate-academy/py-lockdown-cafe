from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("Visitor should be vaccinated")
        if self.is_outdated(vaccine.get("expiration_date")):
            raise OutdatedVaccineError("Visitor should have valid vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor should wear mask")

        return f"Welcome to {self.name}"

    @staticmethod
    def is_outdated(vaccine_expiration_date: date) -> bool:
        return vaccine_expiration_date < date.today()
