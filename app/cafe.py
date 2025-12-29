import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Vaccine is missing")
        else:
            vaccine_date = visitor.get("vaccine").get("expiration_date")
        if vaccine_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("No wearing mask provided")
        return f"Welcome to {self.name}"
