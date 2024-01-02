import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not "
                                     "vaccinated. Access denied.")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine "
                                       "has expired. Access denied.")
        wearing_a_mask = visitor.get("wearing_a_mask", True)
        if not wearing_a_mask:
            raise NotWearingMaskError("Visitor hasn't mask. Access denied.")

        return f"Welcome to {self.name}"
