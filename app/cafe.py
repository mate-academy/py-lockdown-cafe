import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Check if visitor is vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor.get("name", "Visitor")}"
                f" is not vaccinated and cannot enter {self.name}.")

        # Check if the vaccine is expired
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor.get("name", "Visitor")}'s"
                f" vaccine is expired and cannot enter {self.name}.")

        # Check if visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor.get("name", "Visitor")}"
                f" is not wearing a mask and cannot enter {self.name}.")

        return f"Welcome to {self.name}"
