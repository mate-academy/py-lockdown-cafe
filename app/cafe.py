import datetime

from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("You must be vaccinated")
        date_now = datetime.datetime.now()
        if visitor["vaccine"].get("expiration_date") < date_now.date():
            raise OutdatedVaccineError("You must be vaccinated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You must be in a wearing mask")
        return f"Welcome to {self.name}"
