from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{self.name}, you're not vaccinated!")
        if date.today() > visitor.get("vaccine", {}).get("expiration_date"):
            raise OutdatedVaccineError(f"{self.name} "
                                       f"your vaccination is overdue!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{self.name}, please wear a mask!")
        return f"Welcome to {self.name}"
