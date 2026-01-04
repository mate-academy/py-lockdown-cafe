from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self,
                 name: str) -> None:
        self.name = name

    def visit_cafe(self,
                   visitor: dict) -> str:

        visitor_name = visitor["name"]

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor_name} is not vaccinated")

        vaccine = visitor["vaccine"]
        if "expiration_date" not in vaccine:
            raise OutdatedVaccineError(f"{visitor_name} vaccine is unknown")

        vaccine_expiration_date = vaccine["expiration_date"]
        today = date.today()

        if today > vaccine_expiration_date:
            raise OutdatedVaccineError(f"{visitor_name} vaccine is outdated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor_name} is not wearing a mask")

        return f"Welcome to {self.name}"
