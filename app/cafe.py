import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not (vaccine := visitor.get("vaccine")):
            raise NotVaccinatedError("Visitor is not vaccinated")

        if vaccine["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("visitor doesnt not have a mask")

        return f"Welcome to {self.name}"
