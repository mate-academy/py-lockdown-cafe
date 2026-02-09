from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)

import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor should be vaccinated.")
        vaccine_date = visitor["vaccine"]
        if vaccine_date["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The visitor has outdated vaccine.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The visitor should wearing a mask.")
        return f"Welcome to {self.name}"
