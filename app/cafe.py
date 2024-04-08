from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("All visitors must be vaccinated")
        elif visitor["vaccine"].get("expiration_date") < date.today():
            raise OutdatedVaccineError("Vaccine has to be up to date")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear masks")
        return f"Welcome to {self.name}"
