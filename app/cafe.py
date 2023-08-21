from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(
            self,
            name: str
    ) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitors must be vaccinated!")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Your vaccination term is expired!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear a mask!")
        return "Welcome to " + self.name
