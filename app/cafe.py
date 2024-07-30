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
        name = visitor.get("name")
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError(name)
        if vaccine.get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError(name)
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(name)
        return f"Welcome to {self.name}"
