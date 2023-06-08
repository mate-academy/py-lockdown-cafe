from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("You must be vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                "Your vaccination is outdated. It's time for revaccination"
            )
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Your must wear a mask!")

        return f"Welcome to {self.name}"
