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
                f"{visitor.get('name', 'Visitor')} is not vaccinated."
            )

        vaccine_info = visitor["vaccine"]

        expiration_date = vaccine_info.get("expiration_date")
        if expiration_date is None:
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')} has no vaccine "
                f"expiration date."
            )

        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')} "
                f"has invalid expiration date."
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')} "
                f"has an outdated vaccine."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Visitor')} "
                f"is not wearing a mask."
            )

        return f"Welcome to {self.name}"
