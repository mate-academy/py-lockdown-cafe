import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        try:
            self.check_vaccination(visitor)
            self.check_vaccine_expiration(visitor)
            self.check_wearing_a_mask(visitor)
        except (NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError):
            raise
        else:
            return f"Welcome to {self.name}"

    @staticmethod
    def check_vaccine_expiration(visitor: dict) -> None:
        expiration_date = visitor.get("vaccine", {}).get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine has expired")

    @staticmethod
    def check_wearing_a_mask(visitor: dict) -> None:
        if not visitor.get("wearing_a_mask", True):
            raise NotWearingMaskError("Visitor is not wearing a mask")

    @staticmethod
    def check_vaccination(visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
