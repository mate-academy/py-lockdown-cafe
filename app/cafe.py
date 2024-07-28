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
        visitor_name = visitor.get("name", "Unknown Visitor")

        # Check if the visitor is vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor_name)

        # Check if the vaccine is not outdated
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(visitor_name, expiration_date)

        # Check if the visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor_name)

        return f"Welcome to {self.name}"
