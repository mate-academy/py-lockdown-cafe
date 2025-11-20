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
        vaccine = visitor.get("vaccine", None)

        if not vaccine:
            raise NotVaccinatedError("All friends should be vaccinated")

        expiration_date = vaccine.get("expiration_date", None)

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("All friends should be vaccinated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Need to be wearing mask")

        return f"Welcome to {self.name}"
