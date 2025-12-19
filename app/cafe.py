import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor.get("name", "Unknown visitor")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(name)

        expiration_date = visitor["vaccine"].get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(name)

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(name)

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(name)

        return f"Welcome to {self.name}"
