from datetime import date
from typing import Union

from app.errors import (VaccineError,
                        NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict
                   ) -> (str | VaccineError | NotWearingMaskError):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The visitor's vaccine is outdated")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("The visitor is not wearing a mask")
        return f"Welcome to {self.name}"
