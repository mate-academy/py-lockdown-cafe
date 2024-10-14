import datetime
from typing import Dict, Any
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str | Exception:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("You are not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Expired vaccination date")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You should be wearing a mask")
        return f"Welcome to {self.name}"
