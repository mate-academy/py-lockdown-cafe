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
            raise NotVaccinatedError(visitor["name"])

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(visitor["name"])

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(visitor["name"])

        return f"Welcome to {self.name}"
