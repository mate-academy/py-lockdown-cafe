from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor must be vaccinated")
        elif date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("The vaccine should not be expired")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The visitor must wear a mask")

        return f"Welcome to {self.name}"
