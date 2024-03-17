import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor should be vaccinated!")
        expiration_date = visitor.get("vaccine").get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                "The vaccine should have a valid expiration date!"
            )
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "A visitor without a mask will be kicked out!"
            )
        return f"Welcome to {self.name}"
