from datetime import date
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, \
    NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("NotVaccinatedError")
        elif date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("OutdatedVaccineError")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")
        else:
            return f"Welcome to {self.name}"
