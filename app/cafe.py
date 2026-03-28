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
        date = datetime.date.today()
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated!")
        expiration_date = visitor.get("vaccine").get("expiration_date")
        if expiration_date is None or expiration_date < date:
            raise OutdatedVaccineError("Visitor's vaccine is outdated!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is without a mask!")
        return f"Welcome to {self.name}"
