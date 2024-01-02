import datetime
from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from typing import Any


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should be vaccinated")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError(
                f"Expiration date should not be earlier than "
                f"{datetime.date.today()}"
            )
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("All visitors should wear a mask!")
        else:
            return f"Welcome to {self.name}"
