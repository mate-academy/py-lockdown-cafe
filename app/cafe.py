import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {visitor['name']} don't have vaccine."
            )

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor['name']} have expired vaccine."
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"Visitor {visitor['name']} is not wearing mask."
            )
        return f"Welcome to {self.name}"