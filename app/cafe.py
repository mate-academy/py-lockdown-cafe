import datetime
from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: dict) -> any:
        today = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not "
                                     "vaccinated and cannot enter the cafe.")
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("Visitor's vaccine is outdated "
                                       "and cannot enter the cafe")
        if not visitor["wearing_a_mask"] or "wearing_a_mask" not in visitor:
            raise NotWearingMaskError("Visitor is not wearing a mask "
                                      "and cannot enter the cafe.")
        return f"Welcome to {self.name}"
