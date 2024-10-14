import datetime
from errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor should be vaccinated.")
        vaccine_expiration_date = visitor["vaccine"]["expiration_date"]
        today = datetime.date.today()
        if vaccine_expiration_date < today:
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors should wear masks.")
        return f"Welcome to {self.name}"
