from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        if date.today() > visitor.get("vaccine")["expiration_date"]:
            raise OutdatedVaccineError("All friends should be vaccinated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
