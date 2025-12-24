from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']}"
                                     f" must have vaccine")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor['name']}"
                                       f"'s vaccine expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor['name']}"
                                      f" needs to wear a mask")
        return f"Welcome to {self.name}"
