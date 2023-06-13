import datetime
from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError
        expiration_date = vaccine.get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
