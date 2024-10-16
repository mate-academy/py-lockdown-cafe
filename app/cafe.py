from datetime import date
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "You need to be vaccinated to visit the cafe!"
            )
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                "The vaccination has expired!"
            )
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "You need to wear a mask!"
            )
        return f"Welcome to {self.name}"
