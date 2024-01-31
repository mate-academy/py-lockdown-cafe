from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("NotVaccinatedError")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError")
        else:
            return f"Welcome to {self.name}"
