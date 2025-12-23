import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError("Visitor is not vaccinated")
        elif not isinstance(visitor["vaccine"]["expiration_date"],
                            datetime.date):
            raise OutdatedVaccineError("Invalid date format "
                                       "for vaccine expiration")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
