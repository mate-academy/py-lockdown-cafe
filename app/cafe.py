import datetime
from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccine")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMask")
        return f"Welcome to {self.name}"
