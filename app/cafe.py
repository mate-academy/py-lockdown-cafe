from datetime import date
from app.errors import (
    NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("All friends should be vaccinated")
        date_exp = visitor["vaccine"]["expiration_date"]
        if date_exp < date.today():
            raise OutdatedVaccineError("All friends should be vaccinated")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError(
                "Friends should buy {masks_to_buy} masks")
        return f"Welcome to {self.name}"
