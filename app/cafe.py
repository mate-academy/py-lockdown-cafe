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
        # Виносимо ім'я в окрему змінну для скорочення рядків
        visitor_name = visitor.get("name", "Unknown")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {visitor_name} is not vaccinated."
            )

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor_name}'s vaccine is expired."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"Visitor {visitor_name} is not wearing a mask."
            )

        return f"Welcome to {self.name}"
