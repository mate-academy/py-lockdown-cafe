from datetime import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        expiration_date = vaccine.get("expiration_date")
        if isinstance(expiration_date, str):
            expiration_date = datetime.strptime(expiration_date,
                                                "%Y-%m-%d").date()

        if expiration_date < datetime.today().date():
            raise OutdatedVaccineError("Vaccine is outdated.")

        mask = visitor.get("wearing_a_mask")
        if not mask:
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
