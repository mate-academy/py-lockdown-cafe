import datetime
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe():
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Visitor have no vaccine")
        if (visitor["vaccine"].get("expiration_date") is None
                or visitor["vaccine"].get("expiration_date")
                < datetime.date.today()):
            raise OutdatedVaccineError("Visitor's vaccination has expired.")
        if (visitor.get("wearing_a_mask") is None
                or visitor.get("wearing_a_mask") is False):
            raise NotWearingMaskError("Visitor have no wearing mask")
        return f"Welcome to {self.name}"
