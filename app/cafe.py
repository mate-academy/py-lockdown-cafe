import datetime
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine"):
            if visitor["vaccine"]["expiration_date"] >= datetime.date.today():
                if visitor["wearing_a_mask"]:
                    return f"Welcome to {self.name}"
                raise NotWearingMaskError("Visitor is not wearing a mask")
            raise OutdatedVaccineError("Visitor's vaccine is outdated")
        raise NotVaccinatedError("Visitor is not vaccinated")
