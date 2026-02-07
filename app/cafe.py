import datetime
from typing import Any

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated. "
                                     "You can not enter!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine is outdated already. "
                                       "You can not enter!")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You are not wearing a mask! "
                                      "You can not enter")
        return f"Welcome to {self.name}"
