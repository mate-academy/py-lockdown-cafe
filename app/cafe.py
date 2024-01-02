import datetime

from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError
        if datetime.date.today() > visitor["vaccine"].get("expiration_date"):
            raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
