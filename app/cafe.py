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
        visitor_name = visitor.get("name")
        visitor_vaccine = visitor.get("vaccine")

        if not visitor_vaccine:
            raise NotVaccinatedError(f"{visitor_name} does not have a vaccine record and cannot enter.")

        expiration_date = visitor_vaccine.get("expiration_date")
        if isinstance(expiration_date, str):
            expiration_date = date.fromisoformat(expiration_date)

        if expiration_date < date.today():
            raise OutdatedVaccineError(f"{visitor_name}'s vaccine expired on {expiration_date} and is no longer valid.")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor_name} is not wearing a mask and cannot be admitted.")

        return f"Welcome to {self.name}"
