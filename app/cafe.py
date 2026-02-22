import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def visit_cafe(self, visitor: dict) -> str:
        """
        Check if a visitor can enter the cafe.

        Raises:
            NotVaccinatedError: if visitor has no vaccine info
            OutdatedVaccineError: if vaccine expired or missing expiration_date
            NotWearingMaskError: if visitor is not wearing a mask
        Returns:
            str: welcome message if all checks pass
        """
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")
        if not expiration_date or expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                "Vaccine is expired or missing expiration_date"
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
