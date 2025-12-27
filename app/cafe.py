import datetime


from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        temp = visitor["vaccine"]

        if not isinstance(temp, dict) or "expiration_date" not in temp:
            raise ValueError("Invalid vaccine data format")

        expiration_date = temp["expiration_date"]

        if not isinstance(expiration_date, datetime.date):
            raise TypeError("expiration_date should be a datetime.date object")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
