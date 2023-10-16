from errors import (NotVaccinatedError,
                    OutdatedVaccineError,
                    NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("The visitor is not vaccinated.")
        elif visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("The vaccine is outdated.")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("The visitor is not wearing a mask.")
        else:
            return f"Welcome to {self.name}"
