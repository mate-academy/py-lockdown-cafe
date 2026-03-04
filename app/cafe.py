from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("No vaccine")
        expiration_date = visitor.get("vaccine").get("expiration_date")
        if not expiration_date:
            raise TypeError("Empty vaccine dict")
        if expiration_date < date.today():
            raise OutdatedVaccineError("Outdated vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("No mask")
        return f"Welcome to {self.name}"
