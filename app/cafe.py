import datetime
from typing import Union
from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Union[str, None]:
        if visitor.get("vaccine", {}).get("expiration_date") is None:
            raise NotVaccinatedError("The visitor is not vaccinated")
        if datetime.date.today() >\
                visitor.get("vaccine", {}).get("expiration_date"):
            raise OutdatedVaccineError("Overdue vaccination")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The visitor is not wearing a mask")
        return f"Welcome to {self.name}"
