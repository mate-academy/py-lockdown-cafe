import datetime
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"Visitor {visitor['name']}"
                                     f" is not vaccinated.")

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"Visitor {visitor['name']}"
                                       f" has an outdated vaccine.")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"Visitor {visitor['name']}"
                                      f" is not wearing a mask.")

        return f"Welcome to {self.name}"
