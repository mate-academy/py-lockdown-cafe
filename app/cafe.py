from datetime import datetime, date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated.")
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None:
            raise OutdatedVaccineError(
                f"{visitor['name']}'s vaccine expiration date is missing."
            )
        if isinstance(expiration_date, str):
            expiration_date = datetime.strptime(
                expiration_date, "%Y-%m-%d"
            ).date()
        if expiration_date < date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']}'s vaccine is expired."
            )
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing a mask."
            )
        return f"Welcome to {self.name}"
