from .errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
from datetime import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError()
        if visitor["vaccine"]["expiration_date"] < datetime.today().date():
            raise OutdatedVaccineError()
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError()
        else:
            return f"Welcome to {self.name}"
