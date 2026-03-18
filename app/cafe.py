import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        self.get_expiration_date(visitor)
        self.get_wearing_a_mask(visitor)
        return f"Welcome to {self.name}"

    def get_expiration_date(self, visitor: dict) -> datetime.date:
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        return visitor["vaccine"]["expiration_date"]

    def get_wearing_a_mask(self, visitor: dict) -> bool:
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return visitor["wearing_a_mask"]
