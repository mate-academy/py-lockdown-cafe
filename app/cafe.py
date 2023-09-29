import datetime
from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError("All friends should be vaccinated")
        date = visitor["vaccine"].get("expiration_date")
        if date is None or date < datetime.date.today():
            raise OutdatedVaccineError("All friends should be vaccinated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Arsen krasavchik")
        return f"Welcome to {self.name}"
