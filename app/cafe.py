import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You have to be vaccinated.")
        elif visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine is expired.")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You have to be in mask.")
        return f"Welcome to {self.name}"
