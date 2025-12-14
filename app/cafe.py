import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """Check visitor vaccination and mask status."""

        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError(
                f"{visitor.get("name", "Visitor")} is not vaccinated"
            )

        expiration_date = vaccine.get("expiration_date")
        if not expiration_date or not isinstance(expiration_date,
                                                 datetime.date):
            raise OutdatedVaccineError(
                "Vaccine expiration date is missing or invalid"
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor.get("name", "Visitor")} is not wearing a mask"
            )

        return f"Welcome to {self.name}"
