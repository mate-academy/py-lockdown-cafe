import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict, wearing_a_mask: bool = False) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor does not have a vaccine.")

        vaccine = visitor["vaccine"]
        if vaccine["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
