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
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Visitor is not vaccinated")
        if (
            visitor["vaccine"]["expiration_date"] is None
            or visitor["vaccine"]["expiration_date"] < datetime.date.today()
        ):
            raise OutdatedVaccineError("Vaccine of visitor is expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor must have a mask")
        return f"Welcome to {self.name}"
