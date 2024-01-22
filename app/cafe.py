import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor doesn't have a vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The visitor's vaccine has expired")
        if "wearing_a_mask" not in visitor or visitor["wearing_a_mask"] is not True:
            raise NotWearingMaskError("The visitor doesn't have a mask")

        return f"Welcome to {self.name}"
