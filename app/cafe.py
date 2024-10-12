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
            raise NotVaccinatedError("The Person has not been vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine of the person has expired.")
        elif ("wearing_a_mask" not in visitor
              or visitor.get("wearing_a_mask") is False):
            raise NotWearingMaskError("The person is not wearing a mask.")
        return f"Welcome to {self.name}"
