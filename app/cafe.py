from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("wearing_a_mask", True):
            raise (NotWearingMaskError
                   ("The visitor needs to wear a mask"))

        vaccine_info = visitor.get("vaccine")
        if vaccine_info:
            expiration_date = vaccine_info.get("expiration_date")
            if expiration_date < date.today():
                raise (OutdatedVaccineError
                       ("The visitor's vaccine has expired"))
        else:
            raise (NotVaccinatedError
                   ("The visitor is not vaccinated"))

        return f"Welcome to {self.name}"
