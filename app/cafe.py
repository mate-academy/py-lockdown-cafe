from datetime import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        try:
            vaccine = visitor["vaccine"]
        except KeyError:
            raise NotVaccinatedError("Not vaccinated")
            return
        expiration_date = vaccine.get("expiration_date")
        if expiration_date < datetime.today().date():
            raise OutdatedVaccineError("Outdated vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Not wearing mask")
        else:
            return f"Welcome to {self.name}"
