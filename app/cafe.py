import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Not Vaccinated")
        if (visitor["vaccine"].get("expiration_date") is
                None or visitor["vaccine"].get("expiration_date")
                < datetime.date.today()):
            raise OutdatedVaccineError("Outdated Vaccine")
        if (visitor.get("wearing_a_mask") is None
                or visitor.get("wearing_a_mask") is False):
            raise NotWearingMaskError("Not Wearing Mask")
        return f"Welcome to {self.name}"
