from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise (NotVaccinatedError
                   (f"{visitor.get('name', 'Visitor')} is not vaccinated"))

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < date.today():
            raise (OutdatedVaccineError
                   (f"{visitor.get('name', 'Visitor')}'s vaccine is expired"))

        if not visitor.get("wearing_a_mask", False):
            raise (NotWearingMaskError
                   (f"{visitor.get('name', 'Visitor')} is not wearing a mask"))

        return f"Welcome to {self.name}"
