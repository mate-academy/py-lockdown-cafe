import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    """Represents a cafe with pandemic entry rules."""

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """
        Check if a visitor can enter the cafe.

        :param visitor: dict with visitor info
        :return: Welcome message
        :raises NotVaccinatedError: if visitor is not vaccinated
        :raises OutdatedVaccineError: if vaccine expired
        :raises NotWearingMaskError: if visitor not wearing mask
        """
        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError(
                f"Visitor {visitor.get('name', 'Unknown')} is not vaccinated."
            )

        expiration_date = vaccine.get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor.get('name', 'Unknown')} has an expired vaccine."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"Visitor {visitor.get('name', 'Unknown')} is not wearing a mask."
            )

        return f"Welcome to {self.name}"
