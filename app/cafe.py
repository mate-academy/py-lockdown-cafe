from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("message")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("message")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("message")
        return f"Welcome to {self.name}"
