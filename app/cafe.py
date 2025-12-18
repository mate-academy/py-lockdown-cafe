import datetime

from typing import Dict
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict) -> str:
        name: str = visitor.get("name", "Unknown visitor")
        if "vaccine" not in visitor:
            raise NotVaccinatedError(name)

        expiration: datetime.date = visitor["vaccine"].get("expiration_date")
        if expiration is None or expiration < datetime.date.today():
            raise OutdatedVaccineError(name)

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(name)

        return f"Welcome to {self.name}"
