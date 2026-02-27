import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine_key = visitor.get("vaccine")
        if not vaccine_key:
            raise NotVaccinatedError(f"{self.name} you need get vaccine")
        vaccine_date = visitor["vaccine"].get("expiration_date")
        wearing_mask = visitor.get("wearing_a_mask")
        if vaccine_date < datetime.date.today():
            raise OutdatedVaccineError(f"{self.name} your vaccine out of date")
        elif not wearing_mask:
            raise NotWearingMaskError(f"{self.name} you have to buy the mask")
        return f"Welcome to {self.name}"
