from datetime import date
from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You must be vaccinated")
        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("You need booster shot of vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You must wear a mask")
        return f"Welcome to {self.name}"
