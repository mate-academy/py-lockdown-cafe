import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine_info = visitor.get("vaccine")

        if not isinstance(vaccine_info, dict):
            raise NotVaccinatedError("Visitor has no valid vaccine information")

        expiration_date = vaccine_info.get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise NotVaccinatedError("Vaccine expiration date is missing or invalid")

        if datetime.date.today() > expiration_date:
            raise OutdatedVaccineError("Vaccine is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
