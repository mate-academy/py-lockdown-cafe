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
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("need a vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("expired vaccine")
        if visitor["wearing_a_mask"] is not True:
            raise NotWearingMaskError("not wearing mask")
        return f"Welcome to {self.name}"
