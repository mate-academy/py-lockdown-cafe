import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated")
        if visitor["vaccine"].get("expiration_date"):
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Vaccine is expired")
        if (
                not visitor.get("wearing_a_mask")
                or visitor["wearing_a_mask"] is False
        ):
            raise NotWearingMaskError("All visitors must wear masks")
        return f"Welcome to {self.name}"
