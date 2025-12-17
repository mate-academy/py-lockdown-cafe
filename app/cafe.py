import datetime
from .errors import (NotVaccinatedError,
                     OutdatedVaccineError,
                     NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Do vaccine")

        today_date = datetime.date.today()
        vaccine_date = visitor["vaccine"]["expiration_date"]

        if vaccine_date < today_date:
            raise OutdatedVaccineError("Fix your vaccine")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Wear your mask")

        return f"Welcome to {self.name}"
