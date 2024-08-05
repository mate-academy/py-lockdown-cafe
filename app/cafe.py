import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("The visitor doesn't have a vaccine!")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("The visitor's vaccine is outdated!")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("The visitor doesn't have a mask!")

        return f"Welcome to {self.name}"
