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
            raise NotVaccinatedError("We have an error on the line 16.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("We have an error on the line 18.")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("We have an error on the line 20.")

        return f"Welcome to {self.name}"
