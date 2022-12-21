import datetime
from typing import Any
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated")
        if (
            "expiration_date" in visitor["vaccine"]
            and visitor["vaccine"]["expiration_date"] < datetime.date.today()
        ):
            raise OutdatedVaccineError("The vaccine has expired")
        if "wearing_a_mask" in visitor and visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Cafe visitors must wear masks")
        return f"Welcome to {self.name}"
