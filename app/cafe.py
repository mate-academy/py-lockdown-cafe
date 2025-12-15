import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("User is not vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None or expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is missing or expired")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Mask is not worn")

        return f"Welcome to {self.name}"
