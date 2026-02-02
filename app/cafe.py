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
                f"{visitor.get('name', 'Visitor')} is not vaccinated."
            )

        expiration_date = visitor["vaccine"].get("expiration_date")
        if (
                expiration_date is None or not
                isinstance(expiration_date, datetime.date)
        ):
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')} "
                f"vaccine expiration date is missing or invalid."
            )
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')} "
                f"vaccine expired on {expiration_date}.")

        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Visitor')} is not wearing a mask."
            )

        return f"Welcome to {self.name}"
