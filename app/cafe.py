import datetime
from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        visitor_name = visitor.get("name", "Unknown Visitor")
        vaccine_data = visitor.get("vaccine")

        if not vaccine_data:
            raise NotVaccinatedError(f"{visitor_name} is not vaccinated.")

        expiration_date = vaccine_data.get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor_name}'s vaccine is expired.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor_name} is not wearing a mask.")

        return f"Welcome to {self.name}"
