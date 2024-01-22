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
        for _ in visitor:
            if "vaccine" not in visitor:
                raise NotVaccinatedError("All friends should be vaccinated")
            elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("All friends should be vaccinated")
            elif not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("Friends should buy masks")
            else:
                return f"Welcome to {self.name}"
