from datetime import date
from errors import (NotVaccinatedError,
                    OutdatedVaccineError,
                    NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine_exp_date = visitor["vaccine"].get("expiration_date")
        if vaccine_exp_date and vaccine_exp_date < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
