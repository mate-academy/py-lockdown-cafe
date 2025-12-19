import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor.get('name', 'Unknown')} is not vaccinated."
            )

        expiration_date = visitor["vaccine"].get("expiration_date")
        if (not expiration_date
                or not isinstance(expiration_date, datetime.date)):
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Unknown')}'s vaccine expiration date "
                "is invalid or missing."
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Unknown')}'s vaccine is expired."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Unknown')} is not wearing a mask."
            )

        return f"Welcome to {self.name}"
