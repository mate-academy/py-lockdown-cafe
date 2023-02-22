import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Need Vaccine doze")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Do new vaccine doze")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You must buy mask")
        return f"Welcome to {self.name}"
