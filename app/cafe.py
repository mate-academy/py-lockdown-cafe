import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Vaccine is absent")
        expiration = visitor["vaccine"]["expiration_date"]
        if expiration < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired.")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Should wear the mask")
        return f"Welcome to {self.name}"
