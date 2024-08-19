import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Vaccination is required.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Please update the vaccination.")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Wearing a mask is obligatory.")
        return f"Welcome to {self.name}"
