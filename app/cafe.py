import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")

        date = visitor["vaccine"]["expiration_date"]
        current_date = datetime.datetime.now().date()

        if current_date > date:
            raise OutdatedVaccineError("All friends should be vaccinated")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Friends should buy")

        return f"Welcome to {self.name}"
