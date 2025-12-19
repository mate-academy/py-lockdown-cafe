from app.errors import (
    NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor don`t have vaccine!")
        elif datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Vaccine expired")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Please, wear your mask!")
        else:
            return f"Welcome to {self.name}"
