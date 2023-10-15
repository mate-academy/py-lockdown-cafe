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
            raise NotVaccinatedError("Vaccination certificate missing!")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Vaccination certificate outdated!")
        if visitor.get("wearing_a_mask") in (None, False):
            raise NotWearingMaskError("Visitor isn't wearing a mask!")
        return f"Welcome to {self.name}"
