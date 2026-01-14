import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Check if vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor.get("name", "Unknown"))

        # Check if vaccine expired
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None or expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                visitor.get("name", "Unknown"), expiration_date)

        # Check if wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor.get("name", "Unknown"))

        return f"Welcome to {self.name}"
