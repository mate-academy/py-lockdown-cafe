from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        vaccine_info = visitor["vaccine"]
        if vaccine_info["expiration_date"] < date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor must wear a mask.")
        return f"Welcome to {self.name}"
