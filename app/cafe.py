import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Please get vaccinated. ")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("The previous vaccine has expired. ")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Please buy a mask.")
        return f"Welcome to {self.name}"
