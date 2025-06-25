import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor must be vaccinated")

        if "expiration_date" not in visitor["vaccine"]:
            raise TypeError("Not existed key")
        expiration = visitor["vaccine"].get("expiration_date")

        if expiration < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must wear a mask")

        return f"Welcome to {self.name}"
