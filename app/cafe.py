from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated ")
        elif visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("All friends should be vaccinated ")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                "Friends should buy {masks_to_buy} masks"
            )
        return f"Welcome to {self.name}"
