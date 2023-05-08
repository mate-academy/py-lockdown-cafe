import datetime
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        if "wearing_a_mask" not in visitor:
            raise NotWearingMaskError("NotWearingMaskError")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"
