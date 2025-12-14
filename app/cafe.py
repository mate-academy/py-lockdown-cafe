import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine_info = visitor.get("vaccine")
        wearing_mask = visitor.get("wearing_a_mask", True)

        if not vaccine_info:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = vaccine_info.get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        if not wearing_mask:
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
