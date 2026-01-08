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
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor.get('name', 'Visitor')} is not vaccinated"
            )

        expiration_date = visitor["vaccine"].get("expiration_date")

        if isinstance(expiration_date, str):
            expiration_date = datetime.datetime.strptime(
                expiration_date, "%Y-%m-%d"
            ).date()

        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError("Invalid expiration date format")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')}'s vaccine is outdated"
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Visitor')} is not wearing a mask"
            )

        return f"Welcome to {self.name}"
