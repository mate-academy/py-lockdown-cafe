import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine", {})
        expiration_date = vaccine.get("expiration_date")

        if not vaccine:
            raise NotVaccinatedError(
                "All friends should be vaccinated")
        if (not expiration_date
                or expiration_date < datetime.date.today()):
            raise OutdatedVaccineError(
                "All friends should be vaccinated")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "Friends should buy {masks_to_buy} masks")

        return f"Welcome to {self.name}"
