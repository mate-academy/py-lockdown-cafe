from datetime import date

from app.errors import (
    NotVaccinatedError, NotWearingMaskError, OutdatedVaccineError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {self.name} not vaccinated"
            )
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"Visitor {self.name} has an expired vaccination"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"Visitor {self.name} without a "
                f"protective mask on his/her face"
            )
        return f"Welcome to {self.name}"
