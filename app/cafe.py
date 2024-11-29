import datetime

from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor wasn't vaccinated")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Vaccine was outdated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor wasn't wear mask")
        return f"Welcome to {self.name}"
