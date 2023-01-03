import datetime
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("NotVaccinatedError")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")
        else:
            return f"Welcome to {self.name}"
