from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        visitor_name = visitor.get("name")

        if not vaccine:
            raise NotVaccinatedError(
                f"Visitor {visitor_name} is not vaccinated!"
            )

        expiration_date = vaccine.get("expiration_date")
        if expiration_date is None or not isinstance(expiration_date, date):
            raise OutdatedVaccineError(
                f"Visitor {visitor_name} vaccine has expired!"
            )
        if expiration_date < date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor_name} vaccine has expired!"
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"Visitor {visitor_name} is not wearing a mask!"
            )

        return f"Welcome to {self.name}"
