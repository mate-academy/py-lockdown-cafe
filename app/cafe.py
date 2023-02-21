from datetime import date

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(f"{visitor} isn't vaccinated")
        if visitor.get("vaccine")["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor} have outdated vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor} doesn't have a mask")
        return f"Welcome to {self.name}"
