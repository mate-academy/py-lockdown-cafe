from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            vaccine = visitor["vaccine"]
            if vaccine["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("OutdatedVaccineError")
        except KeyError:
            raise NotVaccinatedError("NotVaccinatedError")

        try:
            if visitor["wearing_a_mask"] is False:
                raise NotWearingMaskError("NotWearingMaskError")
        except KeyError:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
