import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        today = datetime.date.today()
        vaccine_exp_date = visitor["vaccine"]["expiration_date"]

        if vaccine_exp_date < today:
            raise OutdatedVaccineError("Vaccine has expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor should wear a mask")

        return f"Welcome to {self.name}"
