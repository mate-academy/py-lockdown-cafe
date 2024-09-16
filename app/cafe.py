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
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Not actual date!")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"{visitor['name']} must be in a mask!")
        return f"Welcome to {self.name}"
