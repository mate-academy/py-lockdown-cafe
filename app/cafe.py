from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("You are not vaccinated")
        if visitor["vaccine"].get("expiration_date") < date.today():
            raise OutdatedVaccineError("You have outdated vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You should wear a mask")
        return f"Welcome to {self.name}"
