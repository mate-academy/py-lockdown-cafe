from datetime import date

from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("visitor should have a vaccine")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("vaccine should not be outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("visitor should wear a mask")
        return f"Welcome to {self.name}"
