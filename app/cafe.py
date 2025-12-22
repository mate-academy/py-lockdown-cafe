from typing import Dict
import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, object]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor["name"]} не вакцинирован.")

        vaccine = visitor["vaccine"]
        if vaccine["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"Вакцина {visitor["name"]} просрочена."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor["name"]} без маски.")

        return f"Welcome to {self.name}"
