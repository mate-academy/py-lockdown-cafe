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
        # Check if visitor has vaccine key
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        # Check if vaccine is not expired
        vaccine_data = visitor["vaccine"]
        expiration_date = vaccine_data["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")

        # Check if visitor is wearing a mask
        # Test expects failure if wearing_a_mask is False or missing
        wearing_mask = visitor.get("wearing_a_mask", False)
        if not wearing_mask:
            raise NotWearingMaskError("Visitor is not wearing a mask")

        # All rules are met
        return f"Welcome to {self.name}"
