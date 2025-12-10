import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Check if visitor is vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor must be vaccinated to enter the cafe")

        # Check if vaccine is not expired
        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired")

        # Check if visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "Visitor must wear a mask to enter the cafe")

        return f"Welcome to {self.name}"
