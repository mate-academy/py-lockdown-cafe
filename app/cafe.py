import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise (OutdatedVaccineError
                   ("The vaccine is past its expiration date."))
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("The visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
