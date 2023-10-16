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
        availability_vaccine = visitor.get("vaccine")
        availability_mask = visitor.get("wearing_a_mask")

        if availability_vaccine:
            expiration_date = availability_vaccine.get("expiration_date")
        else:
            raise NotVaccinatedError

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError
        if not availability_mask:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
