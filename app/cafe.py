import datetime

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        mask = visitor.get("wearing_a_mask")
        today = datetime.date.today()

        if not vaccine:
            raise NotVaccinatedError(f"{self.name} is not vaccinated,")

        if today > vaccine["expiration_date"]:
            raise OutdatedVaccineError(f"{self.name} vaccine is out of date")

        if not mask:
            raise NotWearingMaskError(f"{self.name} should buy masks")

        return f"Welcome to {self.name}"
