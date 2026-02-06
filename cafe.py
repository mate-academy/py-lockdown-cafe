import datetime

from errors import NotVaccinatedError
from errors import OutdatedVaccineError
from errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine_data = visitor["vaccine"]
        expiration_date = vaccine_data.get("expiration_date")

        if expiration_date is None:
            raise OutdatedVaccineError("Vaccine expiration date is missing")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
