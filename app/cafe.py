import datetime
from .errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        current_date = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitors should be vaccinated!")
        elif current_date > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Vaccine shoud be not outdated!")
        elif visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Visitors should wear the mask!")

        return f"Welcome to {self.name}"
