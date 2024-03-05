from datetime import date

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor don't have a vaccine")

        vaccine = visitor["vaccine"]
        if date.today() > vaccine["expiration_date"]:
            raise OutdatedVaccineError("Vaccine is outdated")

        try:
            wearing_a_mask = visitor["wearing_a_mask"]
            if not wearing_a_mask:
                raise ValueError
        except ValueError:
            raise NotWearingMaskError("Visitor don't has a mask")

        return f"Welcome to {self.name}"
