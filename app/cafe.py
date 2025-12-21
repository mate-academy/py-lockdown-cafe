import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Vaccine is not available")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        elif (visitor.get("wearing_a_mask") is None
              or visitor.get("wearing_a_mask") is False):
            raise NotWearingMaskError("Wearing mask is not available")
        else:
            return f"Welcome to {self.name}"
