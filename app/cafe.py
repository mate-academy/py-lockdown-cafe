import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
from typing import Any


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        visitor_name = visitor["name"]

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor_name} is not vaccinated")

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor_name} "
                                       "has an outdated vaccine")

        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor_name} "
                                      "is not wearing a mask")

        else:
            return (f"Welcome to {self.name}")
