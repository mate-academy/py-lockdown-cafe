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
        check = visitor.get("vaccine")
        if not check:
            raise NotVaccinatedError(
                f"{visitor['name']} should be vaccinated"
            )
        date_check = check.get("expiration_date", False)
        if date_check < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']}'s vaccine is outdated"
            )
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor['name']} "
                f"should be wearing a mask inside the {self.name}"
            )
        return f"Welcome to {self.name}"
