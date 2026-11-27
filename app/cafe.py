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
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is unvaccinated.")
        elif visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("Visitor's vaccine is outdated")
        elif (
            "wearing_a_mask" not in visitor
            or visitor["wearing_a_mask"] is False
        ):
            raise NotWearingMaskError("Visitor must wear a mask.")

        return f"Welcome to {self.name}"
