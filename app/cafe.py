import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if not isinstance(visitor["vaccine"].get("expiration_date"), datetime.date):
            raise OutdatedVaccineError("Invalid or missing expiration date in vaccine info.")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is expired.")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        else:
            return f"Welcome to {self.name}"
