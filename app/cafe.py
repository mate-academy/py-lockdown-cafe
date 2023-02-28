import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("NotVaccinatedError")
        elif visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"
