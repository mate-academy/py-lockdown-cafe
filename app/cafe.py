from datetime import date
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        current_date = date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You have no vaccine certificate."
                                     " You shall not pass!")
        if visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError("You have outdated vaccine certificate."
                                       " You shall not pass!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Please put on the mask.")

        return f"Welcome to {self.name}"
