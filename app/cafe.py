import datetime
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "All friends should be vaccinated"
            )

        if datetime.datetime.now().date() > (
                visitor["vaccine"]["expiration_date"]):
            raise OutdatedVaccineError(
                "All friends should be vaccinated"
            )
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "All friends should wear masks"
            )
        return f"Welcome to {self.name}"
