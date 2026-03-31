import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name
        self.date = datetime.date.today()

    def visit_cafe(self, visitor: dict) -> str:

        visitor_name = visitor["name"]

        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor_name)
        if visitor["vaccine"]["expiration_date"] < self.date:
            raise OutdatedVaccineError(visitor_name)
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(visitor_name)
        return f"Welcome to {self.name}"
