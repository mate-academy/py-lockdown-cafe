import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("No vaccine info")
        vaccine = visitor["vaccine"]
        expiration = vaccine.get("expiration_date")
        if (not isinstance(expiration, datetime.date)
                or expiration < datetime.date.today()):
            raise OutdatedVaccineError("Vaccine is missing or expired")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Not wearing a mask")
        return f"Welcome to {self.name}"
