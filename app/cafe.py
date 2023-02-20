import datetime
from typing import Union
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Union[str, None]:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All visitors should be vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors should wear masks")

        return f"Welcome to {self.name}"
