import datetime
from typing import Optional

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Optional[str]:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Denied visit! There is no vaccine!")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Denied visit! Vaccine date not valid!")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Warning! No mask!")
        return f"Welcome to {self.name}"
