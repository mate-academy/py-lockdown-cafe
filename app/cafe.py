import datetime
from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor['name']}, you aren`t vaccinated"
            )
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']}, your vaccine has expired"
            )
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"{visitor['name']}, you should buy a mask"
            )
        return f"Welcome to {self.name}"
