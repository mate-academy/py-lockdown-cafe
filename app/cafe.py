import datetime
from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" in visitor:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Vaccine is expired")
        else:
            raise NotVaccinatedError("Vaccine is required")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Mask is required")

        return f"Welcome to {self.name}"
