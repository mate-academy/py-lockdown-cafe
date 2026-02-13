from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor.get("name") + " must be "
                                     "vaccinated to enter the cafe.")

        expiration_date = visitor["vaccine"].get("expiration_date")

        if expiration_date < date.today():
            raise OutdatedVaccineError(visitor.get("name") + " has an"
                                       " expired vaccine.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(visitor.get("name") + " must wear"
                                      " a mask to enter the cafe.")
        return f"Welcome to {self.name}"
