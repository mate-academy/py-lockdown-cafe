from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        vaccine = visitor["vaccine"]
        if vaccine["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine expiration date is missing.")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor need to wear mask")

        return f"Welcome to {self.name}"
