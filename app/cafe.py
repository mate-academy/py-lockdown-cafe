import datetime

from app.errors import NotVaccinatedError,\
    OutdatedVaccineError,\
    NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor should have vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine has expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("The visitor must wear a mask")
        return f"Welcome to {self.name}"
