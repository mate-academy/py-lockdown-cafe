from datetime import date
from app.errors import (NotWearingMaskError,
                        OutdatedVaccineError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = date.today()
        if "vaccine" not in visitor or not visitor["vaccine"]:
            raise NotVaccinatedError("All friends should be vaccinated")
        if (not visitor["vaccine"]["expiration_date"]
                or visitor["vaccine"]["expiration_date"] < today):
            raise OutdatedVaccineError("All friends should be vaccinated")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Friend is not wearing a mask")

        return f"Welcome to {self.name}"
