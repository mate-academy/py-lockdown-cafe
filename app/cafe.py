import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Person must be vaccinated")
        if (
                datetime.datetime.now().date()
        ) > visitor.get("vaccine").get("expiration_date"):
            raise OutdatedVaccineError("Vaccine expired")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Masks required")
        return f"Welcome to {self.name}"
