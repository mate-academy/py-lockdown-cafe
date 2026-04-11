import datetime
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError
                        )


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor.get('name')} is not vaccinated"
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine has expired.")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must wear a mask.")
        else:
            return f"Welcome to {self.name}"
