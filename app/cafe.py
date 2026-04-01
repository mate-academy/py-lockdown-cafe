import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        if "expiration_date" not in visitor["vaccine"]:
            raise ValueError("Missing expiration date in vaccine information.")

        expiration_date = visitor["vaccine"]["expiration_date"]

        if not isinstance(expiration_date, datetime.date):
            raise ValueError("Invalid expiration date format.")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
