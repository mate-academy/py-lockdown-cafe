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
        customer = visitor["name"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{customer}  does not have a vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{customer} vaccine is out of date")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"{customer} should wear a mask")
        return f"Welcome to {self.name}"
