from datetime import date
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor does not have a vaccine!")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The visitor's vaccine is expired!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The visitor doesn't have a mask!")
        return f"Welcome to {self.name}"
