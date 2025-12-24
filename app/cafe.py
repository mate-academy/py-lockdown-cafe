import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor["name"]

        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError(f"{name} is not vaccinated.")

        expiration_date = vaccine.get("expiration_date")
        if not expiration_date:
            raise OutdatedVaccineError(f"Missing expiration date"
                                       f" for {name}'s vaccine.")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"Vaccine of {name} is expired.")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{name} is not wearing a mask.")

        return f"Welcome to {self.name}"
