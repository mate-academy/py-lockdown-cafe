import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError, OutdatedVaccineError
                        )


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor.get("name", "Unknown visitor")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(name)

        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")

        if expiration_date is None:
            raise OutdatedVaccineError(name)

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(name)

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(name)

        return f"Welcome to {self.name}"
