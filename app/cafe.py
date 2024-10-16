from datetime import date
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                "You need to be vaccinated to visit the cafe!"
            )
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < date.today():
            raise OutdatedVaccineError(
                "The vaccination has expired!"
            )
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "You need to wear a mask!"
            )
        return f"Welcome to {self.name}"
