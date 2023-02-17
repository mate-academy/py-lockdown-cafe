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
        count = 0
        if "vaccine" not in visitor:
            count += 1
            raise NotVaccinatedError(NotVaccinatedError)
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            count += 1
            raise OutdatedVaccineError(OutdatedVaccineError)
        if visitor["wearing_a_mask"] is False:
            count += 1
            raise NotWearingMaskError(NotWearingMaskError)
        if count == 0:
            return f"Welcome to {self.name}"
