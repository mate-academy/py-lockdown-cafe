from datetime import date as dt
from app.Errors.errors import NotVaccinatedError, \
    OutdatedVaccineError, \
    NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should be vaccinated")

        if dt.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Visitor have outdated "
                                       "vaccinated")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor should "
                                      "have mask")
        return f"Welcome to {self.name}"
