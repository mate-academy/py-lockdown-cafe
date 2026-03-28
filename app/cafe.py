from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor)
        date1 = visitor["vaccine"]["expiration_date"]
        date2 = datetime.date.today()
        if date1 < date2:
            raise OutdatedVaccineError(visitor)
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(visitor)
        return f"Welcome to {self.name}"
