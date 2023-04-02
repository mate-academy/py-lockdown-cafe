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
        visitor_name = visitor.get("name")
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(f"Visitor {visitor_name} "
                                     f"is not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor_name}'s vaccine is expired!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor_name} does not wear a mask!")
        return f"Welcome to {self.name}"
