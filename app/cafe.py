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
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                f"{visitor.get('name', 'Visitor')} is not vaccinated"
            )

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None:
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')}'s vaccine is outdated"
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')}'s vaccine is outdated"
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Visitor')} is not wearing a mask"
            )

        return f"Welcome to {self.name}"
