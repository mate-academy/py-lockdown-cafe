import datetime

from app.errors import (
    VaccineError, NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | VaccineError:
        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError
        expiration_date = vaccine.get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError
        mask = visitor.get("wearing_a_mask")
        if mask:
            return f"Welcome to {self.name}"
        raise NotWearingMaskError
