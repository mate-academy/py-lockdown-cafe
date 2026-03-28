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
        wearing_mask = visitor.get("wearing_a_mask")
        if "vaccine" not in visitor:
            raise NotVaccinatedError("one must be vaccinated")
        vaccinated = visitor["vaccine"]
        valid_vaccine = vaccinated.get("expiration_date")
        if valid_vaccine is None or valid_vaccine < datetime.date.today():
            raise OutdatedVaccineError("your vaccine must be valid")
        if not wearing_mask:
            raise NotWearingMaskError("one must wear a mask")
        return f"Welcome to {self.name}"
