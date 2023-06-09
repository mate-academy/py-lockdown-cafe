import datetime

from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                "NotVaccinatedError should be raised with a message")
        current_date = datetime.date.today()
        if visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError(
                "OutdatedVaccineError should be raised with a message")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "NotWearingMaskError should be raised with a message")
        else:
            return f"Welcome to {self.name}"
