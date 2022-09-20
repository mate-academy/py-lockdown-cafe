from datetime import date as dt
from app.Errors.errors import NotVaccinatedError
from app.Errors.errors import OutdatedVaccineError
from app.Errors.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        if dt.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
