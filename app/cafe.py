import datetime
from typing import Any
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> Any:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor is not vaccinated and cannot enter the cafe."
            )

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "Visitor's vaccine is outdated and cannot enter the cafe."
            )

        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                "Visitor is not wearing a mask and cannot enter the cafe."
            )

        else:
            return f"Welcome to {self.name}"
