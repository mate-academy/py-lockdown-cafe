from datetime import date
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            exp_date = visitor["vaccine"]["expiration_date"]
        except KeyError:
            raise NotVaccinatedError("visitor should be vaccinated")
        try:
            assert exp_date >= date.today()
        except AssertionError:
            raise OutdatedVaccineError("your vaccination is outdated ;(")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("visitors are obliged to wear a mask")
        return f"Welcome to {self.name}"
