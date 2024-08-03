from datetime import date
from typing import Any

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                "You should get some vaccine before entering"
            )
        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Your vaccine is out of date")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Please wear a mask")

        return f"Welcome to {self.name}"
